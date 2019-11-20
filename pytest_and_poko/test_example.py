# -*- encoding=utf8 -*-

import os
import pytest

from airtest.core.api import *


def test_level1(device):
    """ This is simple example how we can move test from AirTest IDE to PyTest. """

    assert_exists(Template(r"assets/match_tutorial.png",
                           record_pos=(0.004, -0.05),
                           resolution=(720, 1560)),
                  "Туториал матча отображается")

    touch(Template(r"assets/tutorial_foot.png",
                   target_pos=1, record_pos=(0.003, 0.153),
                   resolution=(720, 1560)))

    assert_exists(Template(r"assets/goal_tutorial.png",
                           record_pos=(0.051, -0.383), resolution=(720, 1560)),
                  "Туториал цели отображается")

    assert_exists(Template(r"assets/continue_button.png",
                           record_pos=(0.056, -0.249), resolution=(720, 1560)),
                  "Кнопка продолжить отображается")

    assert_exists(Template(r"assets/tutorial_arrow_up.png",
                           threshold=0.6499999999999999, rgb=True, record_pos=(0.054, -0.608),
                           resolution=(720, 1560)),
                  "Зеленая стрелка отображается")

    touch(Template(r"assets/continue_button.png",
                   record_pos=(0.056, -0.249), resolution=(720, 1560)))

    assert_exists(Template(r"assets/setting_button.png",
                           record_pos=(-0.425, 0.994), resolution=(720, 1560)),
                  "Кнопка настройки отображается")

    touch(Template(r"assets/setting_button.png",
                   record_pos=(-0.425, 0.994), resolution=(720, 1560)))

    assert_exists(Template(r"assets/music_off.png",
                           record_pos=(-0.415, 0.843), resolution=(720, 1560)),
                  "Музыка выключена")

    assert_exists(Template(r"assets/sounds_off.png",
                           record_pos=(-0.419, 0.701), resolution=(720, 1560)),
                  "Звук выключен")

    assert_exists(Template(r"assets/level_leave_button.png",
                           record_pos=(-0.414, 0.561), resolution=(720, 1560)),
                  "Покинуть уровень")

    touch(Template(r"assets/level_leave_button.png",
                   record_pos=(-0.414, 0.561), resolution=(720, 1560)))

    assert_exists(Template(r"assets/minus_life.png",
                           record_pos=(-0.001, -0.001), resolution=(720, 1560)),
                  "Жизнь -1")

    assert_exists(Template(r"assets/exit_button.png",
                           record_pos=(0.006, 0.454), resolution=(720, 1560)),
                  "Кнопка Выйти'")

    touch(Template(r"assets/exit_button.png",
                   record_pos=(0.006, 0.454), resolution=(720, 1560)))

    wait(Template(r"assets/choose_boosters_locked.png",
                  record_pos=(0.011, 0.242), resolution=(720, 1560)))

    assert_exists(Template(r"assets/choose_boosters_locked.png",
                           record_pos=(0.011, 0.242), resolution=(720, 1560)),
                  "Выбор бустеров заблокирован")

    assert_exists(Template(r"assets/close_button.png",
                           record_pos=(0.419, -0.4), resolution=(720, 1560)),
                  "Кнопка закрытия")

    touch(Template(r"assets/close_button.png",
                   record_pos=(0.419, -0.4), resolution=(720, 1560)))

    touch(Template(r"assets/level_1.png", record_pos=(0.003, 0.689),
                   resolution=(720, 1560)))

    touch(Template(r"assets/play_button.png", record_pos=(-0.001, 0.567),
                   resolution=(720, 1560)))

    touch(Template(r"assets/tutorial_foot.png", target_pos=1,
                   record_pos=(0.003, 0.153), resolution=(720, 1560)))

    touch(Template(r"assets/continue_button.png", record_pos=(0.056, -0.249),
                   resolution=(720, 1560)))

    while not exists(Template(r"assets/continue_button.png",
                              record_pos=(0.056, -0.249), resolution=(720, 1560))):
        try:
            touch(Template(r"assets/2green_upright.png", rgb=True,
                           record_pos=(0.05, 0.007), resolution=(720, 1560)))

            touch(Template(r"assets/2green_horizontal.png",
                           record_pos=(-0.314, 0.115), resolution=(720, 1560)))

            touch(Template(r"assets/2yellow_upright.png", rgb=True,
                           record_pos=(-0.157, 0.211), resolution=(720, 1560)))

            touch(Template(r"assets/2yellow_horizontal.png",
                           record_pos=(0.211, 0.01), resolution=(720, 1560)))

            touch(Template(r"assets/2red_upright.png", rgb=True,
                           record_pos=(-0.053, 0.108), resolution=(720, 1560)))

            touch(Template(r"assets/2red_horizontal.png",
                           record_pos=(-0.208, 0.319), resolution=(720, 1560)))

            touch(Template(r"assets/2blue_upright.png", rgb=True,
                           record_pos=(0.263, 0.325), resolution=(720, 1560)))

            touch(Template(r"assets/2blue_horizontal.png",
                           record_pos=(0.317, -0.096), resolution=(720, 1560)))

            touch(Template(r"assets/2violet_upright.png", record_pos=(0.053, -0.044),
                           resolution=(720, 1560)))

            touch(Template(r"assets/2violet_horizontal.png", record_pos=(0.003, 0.011),
                           resolution=(720, 1560)))
        except:
            pass
