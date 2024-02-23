# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QDialogButtonBox,
                               QPushButton, QProgressDialog, QMessageBox,
                               QDialog, QVBoxLayout, QLabel)
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer, Qt, QThread  #Progress Bar Timinig

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

import epd_logic


from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer

class CustomDialog(QDialog):
    def __init__(self, message, parent=None):
        super(CustomDialog, self).__init__(parent)

        # Set layout
        layout = QVBoxLayout(self)
        label = QLabel(message)

        # Adjusting the size
        label.setMinimumSize(200, 50) # Adjust this to change the size

        # Adjusting the margin
        label.setMargin(10) # Adjust this to change the margin
        label.setLineWidth(4)


        # Change the background to black and text to red
        label.setStyleSheet("QLabel { color : red; background-color : #222; border-radius: 10px }")
        # Change the background color of the dialog to black and border-radius to 3px
        self.setStyleSheet("QDialog { background-color : black; border-radius: 10px;}")

        # Center the text
        label.setAlignment(Qt.AlignCenter)

        # Set the font size to be 12 points and bold
        font = QFont()
        font.setPointSize(12) # Increasing the font-size
        font.setBold(True) # Making the font bold
        label.setFont(font)

        layout.addWidget(label)

        # Set modal
        self.setModal(True)

        # Remove window decorations including close button
        self.setWindowFlag(Qt.FramelessWindowHint, True)

    def dismiss(self):
        self.accept()  # Close the dialog
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logic = epd_logic
        self.ping_thread = QThread()

    def startScanClicked(self):
        dialog = CustomDialog("Scanning....", self)
        
        # Center the dialog
        qr = dialog.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        # dialog.move(qr.topLeft())

        dialog.show()

        # Assuring the dialog shows immediately
        QTimer.singleShot(0, lambda: self.performScan(dialog))

    def performScan(self, dialog):
        # perform the task
        responsiveIp = self.logic.ping_ips()

        # stop the progress dialog
        QTimer.singleShot(0, dialog.dismiss)

        # continue as normal
        self.enableAvailableIps(responsiveIp)

    def enableAvailableIps(self, responsiveIp):
        for pod in responsiveIp:
            hostname = pod['hostname']
            pod_number = hostname.split('-')[-1]  # assuming the hostname is something like 'POD-1'

            # identifying the respective button using the pod number.
            pod_button = getattr(self.ui, f'podButton_{pod_number}', None)

            if pod_button:
                pod_button.setEnabled(True)  # enabling the button if the pod exists
                self.ui.selectionLabel.setText("SELECT AN AVAILABLE POD")
            else:
                print(f"Button for {hostname} not found")

            print(f"enable buttons for: {pod['ip']}, {pod['hostname']}")

    def podClicked(self, button: QPushButton):
        if isinstance(button, QPushButton):
            print(f"did clicked: {button.text()}")

            self.ui.selectionLabel.setText(button.text() + " SELECTED")
            self.ui.detailFrame.setEnabled(True)
            self.ui.nameEdit.setText("")
            self.ui.infoEdit.setText("")

        else:
            print(f"Error: expected QPushButton instance, got {type(button).__name__}")

    def clientInfoEdited(self):
        print(f"clicked: {self.sender}")
        return

    def clientNameEdited(self):
        print(f"clicked: {self.sender}")
        return

    def cancelClicked(self):
        print(f"clicked cancel: {self.sender}")
        quit()

    def acceptClicked(self):
        if not self.ui.nameEdit.text().strip():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Name field must be filled out")
            msg.setWindowTitle("Missing Data")
            msg.exec()
        else:
            print(f"clicked accept: {self.ui.nameEdit.text()}")
            self.logic.data_entry(self, pod="POD-1", ip="192.168.1.151", 
                                  name=self.ui.nameEdit.text(), info=self.ui.infoEdit.text())

        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
