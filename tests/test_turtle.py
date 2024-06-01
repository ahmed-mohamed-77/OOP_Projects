import pytest
from unittest.mock import patch, call
from turtle import Turtle
from oo_projects.source.turtle_objectives import main, hollow_pentagon, solid_squares, circle_canvas, triangle_canvas

@pytest.fixture
def mock_turtle():
    with patch('oo_projects.source.turtle_objectives.Turtle') as mock_turtle:
        yield mock_turtle

@pytest.fixture
def mock_hollow_pentagon():
    with patch('oo_projects.source.turtle_objectives.hollow_pentagon') as mock_hollow_pentagon:
        yield mock_hollow_pentagon

@pytest.fixture
def mock_solid_squares():
    with patch('oo_projects.source.turtle_objectives.solid_squares') as mock_solid_squares:
        yield mock_solid_squares

@pytest.fixture
def mock_circle_canvas():
    with patch('oo_projects.source.turtle_objectives.circle_canvas') as mock_circle_canvas:
        yield mock_circle_canvas

@pytest.fixture
def mock_triangle_canvas():
    with patch('oo_projects.source.turtle_objectives.triangle_canvas') as mock_triangle_canvas:
        yield mock_triangle_canvas

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock_print:
        yield mock_print

def test_draw_pentagon(mock_turtle, mock_hollow_pentagon):
    with patch('builtins.input', side_effect=['pentagon', 'exit']):
        main()
        mock_hollow_pentagon.assert_called_once()

def test_draw_squares(mock_turtle, mock_solid_squares):
    with patch('builtins.input', side_effect=['square', '3', 'exit']):
        main()
        mock_solid_squares.assert_called_once()

def test_draw_circles(mock_turtle, mock_circle_canvas):
    with patch('builtins.input', side_effect=['circle', '4', 'exit']):
        main()
        mock_circle_canvas.assert_called_once()

def test_draw_triangles(mock_turtle, mock_triangle_canvas):
    with patch('builtins.input', side_effect=['triangle', '5', 'exit']):
        main()
        mock_triangle_canvas.assert_called_once()

def test_invalid_input(mock_print):
    with patch('builtins.input', side_effect=['hexagon', 'exit']):
        main()
        mock_print.assert_any_call("\nERROR PLEASE SELECT FROM THE GIVEN SHAPES\n")
        mock_print.assert_any_call("*" * 30)

def test_non_positive_number(mock_print):
    with patch('builtins.input', side_effect=['square', '-3', 'exit']):
        main()
        for call in mock_print.call_args_list:
            print(call)  # Debugging print to see what calls were made
        mock_print.assert_any_call("\nERROR MUST BE POSITIVE NUMBER\n")
        mock_print.assert_any_call("*" * 30)
