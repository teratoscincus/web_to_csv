"""Main entry point."""

from web_to_csv.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
