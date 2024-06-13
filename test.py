from nicegui import ui


def main():
    # Define the main function to create the UI
    with ui.column:
        # Add a label to the UI
        ui.label("Click the icon to navigate.")

        # Wrap the icon inside a link
        with ui.link("https://www.example.com"):
            ui.icon("mdi-earth")

    # Run the UI


# Call the main function to run the application
ui.run()
