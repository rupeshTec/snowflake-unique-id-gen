# snowflake.py

import time
import threading

#TODO: Implement for distributed systems
class SnowflakeGenerator:
    def __init__(self, machine_id: int):
        # Config
        self.epoch = 1672531200000  # Jan 1, 2023 in ms
        self.machine_id_bits = 10
        self.sequence_bits = 12

        self.max_machine_id = -1 ^ (-1 << self.machine_id_bits)  # 1023
        self.max_sequence = -1 ^ (-1 << self.sequence_bits)      # 4095

        if machine_id < 0 or machine_id > self.max_machine_id:
            raise ValueError(f"Machine ID must be between 0 and {self.max_machine_id}")

        self.machine_id = machine_id
        self.sequence = 0
        self.last_timestamp = -1

        # Bit shifts
        self.timestamp_shift = self.machine_id_bits + self.sequence_bits
        self.machine_shift = self.sequence_bits

        self.lock = threading.Lock()

    def _current_millis(self):
        return int(time.time() * 1000)

    def _wait_next_millis(self, last_timestamp):
        timestamp = self._current_millis()
        while timestamp <= last_timestamp:
            timestamp = self._current_millis()
        return timestamp

    def generate_id(self):
        with self.lock:
            timestamp = self._current_millis()

            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards. Refusing to generate id")

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self.max_sequence
                if self.sequence == 0:
                    timestamp = self._wait_next_millis(self.last_timestamp)
            else:
                self.sequence = 0

            self.last_timestamp = timestamp

            id = ((timestamp - self.epoch) << self.timestamp_shift) | \
                 (self.machine_id << self.machine_shift) | \
                 self.sequence

            return id
