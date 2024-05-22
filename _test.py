import pytest
from unittest.mock import Mock, patch
from main import start_bubble_sort, start_flappy_bird, open_webpage

@patch('main.BubbleSort')
@patch('main.root')
def test_start_bubble_sort(mock_root, mock_bubble_sort):
    start_bubble_sort()
    mock_root.destroy.assert_called_once()
    mock_bubble_sort.assert_called_once()

@patch('main.gameUI')
@patch('main.root')
def test_start_flappy_bird(mock_root, mock_gameUI):
    start_flappy_bird()
    mock_root.destroy.assert_called_once()
    mock_gameUI.assert_called_once()

@patch('main.webbrowser')
def test_open_webpage(mock_webbrowser):
    open_webpage()
    mock_webbrowser.open.assert_called_once_with('https://github.com/mehmetkahya0', new=2)
    
