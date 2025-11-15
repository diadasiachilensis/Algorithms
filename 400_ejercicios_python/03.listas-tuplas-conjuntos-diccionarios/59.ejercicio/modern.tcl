ttk::style theme create modern -parent default -settings {

    # Colors
    set bg_main       "#F5F7FA"
    set bg_panel      "#FFFFFF"
    set accent        "#4A90E2"
    set accent_dark   "#357ABD"
    set text_dark     "#333333"
    set border_color  "#D0D4D9"

    # Global settings
    ttk::style configure . \
        -background $bg_main \
        -foreground $text_dark \
        -font {Segoe UI 10}

    # Buttons
    ttk::style configure TButton \
        -padding 8 \
        -background $accent \
        -foreground white \
        -borderwidth 0 \
        -font {Segoe UI 10 bold}

    ttk::style map TButton \
        -background [list active $accent_dark disabled $border_color]

    # Accent button (super important)
    ttk::style configure AccentButton \
        -padding 10 \
        -background "#5AC18E" \
        -foreground white \
        -borderwidth 0 \
        -font {Segoe UI 10 bold}

    ttk::style map AccentButton \
        -background [list active "#4CAF84" disabled "#D0D4D9"]

    # Labels
    ttk::style configure TLabel \
        -background $bg_main \
        -foreground $text_dark \
        -font {Segoe UI 10}

    # Entries
    ttk::style configure TEntry \
        -padding 6 \
        -foreground $text_dark \
        -fieldbackground $bg_panel \
        -bordercolor $border_color

    # Treeview
    ttk::style configure Treeview \
        -background $bg_panel \
        -fieldbackground $bg_panel \
        -foreground $text_dark \
        -bordercolor $border_color

    ttk::style configure Treeview.Heading \
        -font {Segoe UI 10 bold} \
        -foreground $text_dark

    # Frames
    ttk::style configure TFrame \
        -background $bg_main
}