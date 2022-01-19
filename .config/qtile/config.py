from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
mod = "mod4"
terminal = "alacritty"
BLACK = "000000"
GREEN = "8fbc8f"
BLUE = "6790EB"
RED = "8b0000"
WHITE = "ffffff"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "m", lazy.spawn('"/home/el/Applications/Lunar Client-2.9.3.AppImage" --no-sandbox %U')),
    Key([mod], "b", lazy.spawn("chromium")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "o", lazy.spawn("wps")),
    Key([mod], "q", lazy.spawn("clearine")),
    Key([mod], "c", lazy.spawn("discord")),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]


groups = (
    Group('1', label='⬤'),
    Group('2', label='⬤'),
    Group('3', label='⬤'),
    Group('4', label='⬤'),
    Group('5', label='⬤'),
    Group('6', label='⬤'),
    Group('7', label='⬤'),
    Group('8', label='⬤'),
)
dgroups_key_binder = simple_key_binder("mod4")


layout_theme = {"border_width": 5,
                "margin": 6,
               "border_focus": GREEN,
                "border_normal": BLACK
                }
layouts = [

    layout.Bsp(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    ]


widget_defaults = dict(
    font='SauceCodePro Nerd Font Mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.Spacer(length=15),
                widget.CurrentLayoutIcon(),
                widget.GroupBox(fontsize=15, this_current_screen_border=GREEN),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Spacer(length=10),
                widget.TextBox(text='🎧'),
                widget.PulseVolume(),
                widget.Spacer(length=10),
                widget.TextBox(text='🔋'),
                widget.Battery(format='{char} {percent:2.0%}'),
                widget.Spacer(length=15),
                widget.Clock(format='%d %a %I:%M %p'),
                widget.Spacer(length=15),
            ],
            24,
opacity=.7
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "qtile"

