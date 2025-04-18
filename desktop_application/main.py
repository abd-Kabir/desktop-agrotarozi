import sys
import os
import django

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Start Django server thread
# django_thread = threading.Thread(target=run_django, daemon=True)
# django_thread.start()


class WebApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Django + PyQt5 Serial Reader")
        self.setGeometry(100, 100, 1024, 768)

        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:7000/"))  # ✅ Use QUrl
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebApp()
    window.show()
    sys.exit(app.exec_())
