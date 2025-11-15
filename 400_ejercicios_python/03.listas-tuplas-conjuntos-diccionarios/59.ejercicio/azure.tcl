# Create azure.tcl file with Azure theme content
content = """
# Azure theme for Tkinter Ttk
ttk::style theme create azure -parent default -settings {
    ttk::style configure TButton -padding 10 -foreground #ffffff -background #0078D4 -font {Segoe UI 10 bold}
    ttk::style map TButton -background {
        active #005A9E
        disabled #A6A6A6
    }
    ttk::style configure AccentButton -padding 10 -foreground #ffffff -background #0063B1
    ttk::style map AccentButton -background {
        active #005A9E
        disabled #A6A6A6
    }
    ttk::style configure Treeview -background #ffffff -fieldbackground #ffffff -foreground #000000
    ttk::style configure Treeview.Heading -font {Segoe UI 10 bold}
}
"""
with open('/mnt/data/azure.tcl','w') as f:
    f.write(content)

'/mnt/data/azure.tcl'
