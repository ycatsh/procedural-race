import pygame
import random

from constants import *


class Track:
    def __init__(self, screen_width, screen_height):
        self.segments = self.init_segments(screen_width, screen_height)

    def init_segments(self, screen_width, screen_height):
        segments = []
        base_x = screen_width // 2 - TRACK_WIDTH // 2

        for i in range((screen_height // SEGMENT_HEIGHT) + 10):
            jitter = random.choice([-20, -10, 0, 10, 20])
            left_x = max(TRACK_MARGIN, min(screen_width - TRACK_WIDTH - TRACK_MARGIN, base_x + jitter))
            segments.append([left_x, screen_height - i * SEGMENT_HEIGHT])

        return segments

    def append_segment(self, screen_width):
        prev_left_x = self.segments[-1][0]
        shift = random.choice(SHIFT_OPTIONS)
        new_left_x = max(TRACK_MARGIN, min(screen_width - TRACK_WIDTH - TRACK_MARGIN, prev_left_x + shift))
        self.segments.append([new_left_x, self.segments[-1][1] - SEGMENT_HEIGHT])

    def update(self, screen_width, screen_height):
        for seg in self.segments:
            seg[1] += SCROLL_SPEED
            
        if self.segments[0][1] > screen_height:
            self.segments.pop(0)
            self.append_segment(screen_width)

    def get_edges_at_car(self, car_y):
        for left_x, seg_y in self.segments:
            if seg_y <= car_y and car_y < (seg_y + SEGMENT_HEIGHT):
                right_x = left_x + TRACK_WIDTH
                return left_x, right_x
        return 0, 0

    def draw(self, screen, screen_width):
        for left_x, y in self.segments:
            right_x = left_x + TRACK_WIDTH
            pygame.draw.rect(screen, BLACK, (0, y, left_x, SEGMENT_HEIGHT))
            pygame.draw.rect(screen, BLACK, (right_x, y, screen_width - right_x, SEGMENT_HEIGHT))
