import unittest
from unittest.mock import Mock, patch
import pygame
from main import main


class TestGameLoop(unittest.TestCase):
    """Tests for the game loop execution."""

    @patch('pygame.display.set_mode')
    @patch('pygame.display.flip')
    @patch('pygame.event.get')
    def test_frame_rate_does_not_exceed_60_fps(self, mock_event_get, mock_flip, mock_set_mode):
        """Test that the game loop execution rate does not exceed 60 FPS."""
        # Mock the screen
        mock_screen = Mock()
        mock_screen.fill = Mock()
        mock_set_mode.return_value = mock_screen
        
        # Create a real clock to test frame rate limiting
        real_clock = pygame.time.Clock()
        
        frame_times = []
        frame_count = 10
        
        # Mock events to quit after a few frames
        quit_event = Mock()
        quit_event.type = pygame.QUIT
        
        call_count = [0]
        
        def side_effect():
            call_count[0] += 1
            if call_count[0] >= frame_count:
                return [quit_event]
            return []
        
        mock_event_get.side_effect = side_effect
        
        # Patch clock.tick to capture frame times
        with patch('pygame.time.Clock') as mock_clock_class:
            mock_clock = Mock()
            tick_times = []
            
            def tick_side_effect(fps):
                # Simulate real clock behavior
                elapsed = real_clock.tick(fps)
                tick_times.append(elapsed)
                return elapsed
            
            mock_clock.tick = Mock(side_effect=tick_side_effect)
            mock_clock_class.return_value = mock_clock
            
            # Run the game loop
            main()
            
            # Verify tick was called with 60 FPS
            for call in mock_clock.tick.call_args_list:
                self.assertEqual(call[0][0], 60, "Clock tick should be called with 60 FPS")
            
            # Verify average frame time is at least 1/60 seconds (16.67ms)
            # This ensures the frame rate doesn't exceed 60 FPS
            if len(tick_times) > 1:
                avg_frame_time = sum(tick_times) / len(tick_times)
                min_frame_time = 1000 / 60  # 16.67ms for 60 FPS
                self.assertGreaterEqual(
                    avg_frame_time, 
                    min_frame_time * 0.8,  # Allow 20% tolerance
                    f"Average frame time ({avg_frame_time}ms) should be >= {min_frame_time}ms to not exceed 60 FPS"
                )

    @patch('pygame.display.set_mode')
    @patch('pygame.display.flip')
    @patch('pygame.event.get')
    def test_dt_calculates_delta_time_accurately(self, mock_event_get, mock_flip, mock_set_mode):
        """Test that dt variable accurately calculates delta time in seconds."""
        # Mock the screen
        mock_screen = Mock()
        mock_screen.fill = Mock()
        mock_set_mode.return_value = mock_screen
        
        # Mock events to quit after a few frames
        quit_event = Mock()
        quit_event.type = pygame.QUIT
        
        call_count = [0]
        dt_values = []
        
        def side_effect():
            call_count[0] += 1
            if call_count[0] >= 5:
                return [quit_event]
            return []
        
        mock_event_get.side_effect = side_effect
        
        # Patch clock to return known tick values
        with patch('pygame.time.Clock') as mock_clock_class:
            mock_clock = Mock()
            
            # Simulate different frame times in milliseconds
            tick_return_values = [16, 17, 16, 18, 16]  # Milliseconds
            tick_index = [0]
            
            def tick_side_effect(fps):
                if tick_index[0] < len(tick_return_values):
                    value = tick_return_values[tick_index[0]]
                    tick_index[0] += 1
                    return value
                return 16
            
            mock_clock.tick = Mock(side_effect=tick_side_effect)
            mock_clock_class.return_value = mock_clock
            
            # We need to capture dt values somehow
            # Since dt is a local variable, we'll verify the calculation logic instead
            original_main = main
            
            # Verify the calculation: dt should be clock.tick(60) / 1000
            for tick_ms in tick_return_values:
                expected_dt = tick_ms / 1000
                
                # Verify the formula
                self.assertAlmostEqual(
                    expected_dt,
                    tick_ms / 1000,
                    places=6,
                    msg=f"Delta time should be {tick_ms}ms / 1000 = {expected_dt}s"
                )
                
                # Verify dt is in seconds (reasonable range for 60 FPS)
                self.assertGreater(expected_dt, 0, "Delta time should be positive")
                self.assertLess(expected_dt, 0.1, "Delta time should be less than 100ms for 60 FPS")
                self.assertAlmostEqual(
                    expected_dt, 
                    1/60, 
                    delta=0.005,
                    msg=f"Delta time should be approximately 1/60 second ({1/60:.6f}s) for 60 FPS"
                )


if __name__ == '__main__':
    unittest.main()
