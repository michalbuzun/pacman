from obstacle import Obstacle


def test_check_if_in_game_field_far_to_right():
    obstacle = Obstacle()
    position = (750, 200)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is True


def test_is_in_game_field_far_to_right_to_far():
    obstacle = Obstacle()
    position = (800, 200)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is False


def test_is_in_game_field_far_to_left():
    obstacle = Obstacle()
    position = (0, 200)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is True


def test_is_in_game_field_far_to_left_to_far():
    obstacle = Obstacle()
    position = (-50, 200)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is False


def test_is_in_game_field_far_to_top():
    obstacle = Obstacle()
    position = (300, 0)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is True


def test_is_in_game_field_far_to_top_to_far():
    obstacle = Obstacle()
    position = (300, -50)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is False


def test_is_in_game_field_far_to_bottom():
    obstacle = Obstacle()
    position = (300, 400)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is True


def test_is_in_game_field_far_to_the_bottom_to_far():
    obstacle = Obstacle()
    position = (300, 450)

    is_out_of_game_field = obstacle._is_in_game_field(position)

    assert is_out_of_game_field is False


def test_is_in_possible_moves():
    obstacle = Obstacle()
    position = (100, 350)

    is_wall_hit = obstacle._is_in_possible_moves(position)

    assert is_wall_hit is False


def test_is_in_possible_moves_not_hitted():
    obstacle = Obstacle()
    position = (100, 400)

    is_wall_hit = obstacle._is_in_possible_moves(position)

    assert is_wall_hit is True
