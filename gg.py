import sys, tkinter, pygame, mutagen, os, warnings, time
from tkinter import filedialog
from mutagen import File
from mutagen.easyid3 import EasyID3
from PyLyrics import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from mutagen.mp3 import MP3, MPEGInfo
from PySide2 import QtCore, QtGui

'''
Contents: class - line(s)

QJumpSlider class - 24~36
Track class       - 38~42
Graphics class    - 44~232
BlackTheme class  - 234~312
BlueTheme class   - 314~392
PinkTheme class   - 394~472
WhiteTheme class  - 474~552
MusicPlayer class - 554~1324
'''





class Track():
    def __init__(self, length, title, path):
        self.length = length
        self.title = title
        self.path = path


class Graphics(object):
    def setupUi(self, MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        self.x = root.winfo_screenwidth() / 1920
        self.y = root.winfo_screenheight() / 1080
        self.playlistWindowFontSize = 9.3
        self.lyricsWindowFontSize = 8.5
        self.generalFontSize = 8.6
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125 * self.x, 865 * self.y)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playlistWindow = QtGui.QListView(self.centralwidget)
        self.playlistWindow.setGeometry(QtCore.QRect(10 * self.x, 40 * self.y, 301 * self.x, 801 * self.y))
        self.playlistWindow.setObjectName("playlistWindow")
        self.font = self.playlistWindow.font()
        self.font.setPointSizeF(self.playlistWindowFontSize * self.y)
        self.playlistWindow.setFont(self.font)
        self.lyricsWindow = QtGui.QTextBrowser(self.centralwidget)
        self.lyricsWindow.setGeometry(QtCore.QRect(810 * self.x, 40 * self.y, 301 * self.x, 801 * self.y))
        self.lyricsWindow.setObjectName("lyricsWindow")
        self.font = self.lyricsWindow.font()
        self.font.setPointSizeF(self.lyricsWindowFontSize * self.y)
        self.lyricsWindow.setFont(self.font)
        self.albumArt = QtGui.QGraphicsView(self.centralwidget)
        self.albumArt.setGeometry(QtCore.QRect(325 * self.x, 40 * self.y, 471 * self.x, 431 * self.y))
        self.albumArt.setObjectName("albumArt")
        self.openFileButton = QtGui.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(523 * self.x, 10 * self.y, 75 * self.x, 23 * self.y))
        self.openFileButton.setObjectName("openFileButton")
        self.songName = QtGui.QLabel(self.centralwidget)
        self.songName.setGeometry(QtCore.QRect(330 * self.x, 640 * self.y, 461 * self.x, 21 * self.y))
        self.songName.setObjectName("songName")
        self.font = self.songName.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.songName.setFont(self.font)
        self.artistName = QtGui.QLabel(self.centralwidget)
        self.artistName.setGeometry(QtCore.QRect(330 * self.x, 670 * self.y, 461 * self.x, 21 * self.y))
        self.artistName.setObjectName("artistName")
        self.font = self.artistName.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.artistName.setFont(self.font)
        self.albumName = QtGui.QLabel(self.centralwidget)
        self.albumName.setGeometry(QtCore.QRect(330 * self.x, 700 * self.y, 461 * self.x, 21 * self.y))
        self.albumName.setObjectName("albumName")
        self.font = self.albumName.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.albumName.setFont(self.font)
        self.songsCount = QtGui.QLabel(self.centralwidget)
        self.songsCount.setGeometry(QtCore.QRect(740 * self.x, 670 * self.y, 61 * self.x, 21 * self.y))
        self.songsCount.setObjectName("songsCount")
        self.font = self.songsCount.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.songsCount.setFont(self.font)
        self.seekSlider = QJumpSlider(self.centralwidget)
        self.seekSlider.setGeometry(QtCore.QRect(330 * self.x, 500 * self.y, 461 * self.x, 22 * self.y))
        self.seekSlider.setOrientation(QtCore.Qt.Horizontal)
        self.seekSlider.setObjectName("seekSlider")
        self.volumeSlider = QtGui.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(330 * self.x, 780 * self.y, 461 * self.x, 22 * self.y))
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.seekLabel = QtGui.QLabel(self.centralwidget)
        self.seekLabel.setGeometry(QtCore.QRect(330 * self.x, 480 * self.y, 461 * self.x, 20 * self.y))
        self.seekLabel.setObjectName("seekLabel")
        self.font = self.seekLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.seekLabel.setFont(self.font)
        self.prevSongButton = QtGui.QPushButton(self.centralwidget)
        self.prevSongButton.setGeometry(QtCore.QRect(440 * self.x, 550 * self.y, 71 * self.x, 71 * self.y))
        self.prevSongButton.setText("")
        self.prevSongButton.setIconSize(QtCore.QSize(80 * self.x, 80 * self.y))
        self.prevSongButton.setObjectName("prevSongButton")
        self.playPauseButton = QtGui.QPushButton(self.centralwidget)
        self.playPauseButton.setGeometry(QtCore.QRect(520 * self.x, 550 * self.y, 81 * self.x, 71 * self.y))
        self.playPauseButton.setText("")
        self.playPauseButton.setIconSize(QtCore.QSize(80 * self.x, 80 * self.y))
        self.playPauseButton.setObjectName("playPauseButton")
        self.nextSongButton = QtGui.QPushButton(self.centralwidget)
        self.nextSongButton.setGeometry(QtCore.QRect(610 * self.x, 550 * self.y, 71 * self.x, 71 * self.y))
        self.nextSongButton.setText("")
        self.nextSongButton.setIconSize(QtCore.QSize(80 * self.x, 80 * self.y))
        self.nextSongButton.setObjectName("nextSongButton")
        self.volumeLabel = QtGui.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(330 * self.x, 760 * self.y, 461 * self.x, 20 * self.y))
        self.volumeLabel.setObjectName("volumeLabel")
        self.font = self.volumeLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.volumeLabel.setFont(self.font)
        self.minVolLabel = QtGui.QLabel(self.centralwidget)
        self.minVolLabel.setGeometry(QtCore.QRect(330 * self.x, 810 * self.y, 21 * self.x, 21 * self.y))
        self.minVolLabel.setObjectName("minVolLabel")
        self.font = self.minVolLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.minVolLabel.setFont(self.font)
        self.maxVolLabel = QtGui.QLabel(self.centralwidget)
        self.maxVolLabel.setGeometry(QtCore.QRect(760 * self.x, 810 * self.y, 41 * self.x, 21 * self.y))
        self.maxVolLabel.setObjectName("maxVolLabel")
        self.font = self.maxVolLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.maxVolLabel.setFont(self.font)
        self.curVolLabel = QtGui.QLabel(self.centralwidget)
        self.curVolLabel.setGeometry(QtCore.QRect(540 * self.x, 810 * self.y, 41 * self.x, 21 * self.y))
        self.curVolLabel.setObjectName("curVolLabel")
        self.font = self.curVolLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.curVolLabel.setFont(self.font)
        self.playlistLabel = QtGui.QLabel(self.centralwidget)
        self.playlistLabel.setGeometry(QtCore.QRect(10 * self.x, 10 * self.y, 301 * self.x, 21 * self.y))
        self.playlistLabel.setObjectName("playlistLabel")
        self.font = self.playlistLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.playlistLabel.setFont(self.font)
        self.lyricsLabel = QtGui.QLabel(self.centralwidget)
        self.lyricsLabel.setGeometry(QtCore.QRect(810 * self.x, 10 * self.y, 301 * self.x, 21 * self.y))
        self.lyricsLabel.setObjectName("lyricsLabel")
        self.font = self.lyricsLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.lyricsLabel.setFont(self.font)
        self.totalSongTimeLabel = QtGui.QLabel(self.centralwidget)
        self.totalSongTimeLabel.setGeometry(QtCore.QRect(760 * self.x, 520 * self.y, 41 * self.x, 21 * self.y))
        self.totalSongTimeLabel.setObjectName("totalSongTimeLabel")
        self.font = self.totalSongTimeLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.totalSongTimeLabel.setFont(self.font)
        self.curSongTimeLabel = QtGui.QLabel(self.centralwidget)
        self.curSongTimeLabel.setGeometry(QtCore.QRect(320 * self.x, 520 * self.y, 41 * self.x, 21 * self.y))
        self.curSongTimeLabel.setObjectName("curSongTimeLabel")
        self.font = self.curSongTimeLabel.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.curSongTimeLabel.setFont(self.font)
        self.blackThemeButton = QtGui.QPushButton(self.centralwidget)
        self.blackThemeButton.setGeometry(QtCore.QRect(330 * self.x, 10 * self.y, 71 * self.x, 23 * self.y))
        self.blackThemeButton.setObjectName("blackThemeButton")
        self.font = self.blackThemeButton.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.blackThemeButton.setFont(self.font)
        self.blueThemeButton = QtGui.QPushButton(self.centralwidget)
        self.blueThemeButton.setGeometry(QtCore.QRect(410 * self.x, 10 * self.y, 71 * self.x, 23 * self.y))
        self.blueThemeButton.setObjectName("blueThemeButton")
        self.font = self.blueThemeButton.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.blueThemeButton.setFont(self.font)
        self.whiteThemeButton = QtGui.QPushButton(self.centralwidget)
        self.whiteThemeButton.setGeometry(QtCore.QRect(720 * self.x, 10 * self.y, 71 * self.x, 23 * self.y))
        self.whiteThemeButton.setObjectName("whiteThemeButton")
        self.font = self.whiteThemeButton.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.whiteThemeButton.setFont(self.font)
        self.pinkThemeButton = QtGui.QPushButton(self.centralwidget)
        self.pinkThemeButton.setGeometry(QtCore.QRect(640 * self.x, 10 * self.y, 71 * self.x, 23 * self.y))
        self.pinkThemeButton.setObjectName("pinkThemeButton")
        self.font = self.pinkThemeButton.font()
        self.font.setPointSizeF(self.generalFontSize * self.y)
        self.pinkThemeButton.setFont(self.font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "Snake MP3 Player", None, QtGui.QApplication.UnicodeUTF8))
        self.lyricsWindow.setHtml(QtGui.QApplication.translate("MainWindow",
                                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                               None, QtGui.QApplication.UnicodeUTF8))
        self.openFileButton.setText(
            QtGui.QApplication.translate("MainWindow", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.songName.setText(
            QtGui.QApplication.translate("MainWindow", "Song:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.artistName.setText(
            QtGui.QApplication.translate("MainWindow", "Artist:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.albumName.setText(
            QtGui.QApplication.translate("MainWindow", "Album: ", None, QtGui.QApplication.UnicodeUTF8))
        self.songsCount.setText(
            QtGui.QApplication.translate("MainWindow", "0 / 0", None, QtGui.QApplication.UnicodeUTF8))
        self.seekLabel.setText(
            QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">Seek</p></body></html>",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.volumeLabel.setText(QtGui.QApplication.translate("MainWindow",
                                                              "<html><head/><body><p align=\"center\">Volume</p></body></html>",
                                                              None, QtGui.QApplication.UnicodeUTF8))
        self.minVolLabel.setText(
            QtGui.QApplication.translate("MainWindow", "0 %", None, QtGui.QApplication.UnicodeUTF8))
        self.maxVolLabel.setText(
            QtGui.QApplication.translate("MainWindow", "100 %", None, QtGui.QApplication.UnicodeUTF8))
        self.curVolLabel.setText(
            QtGui.QApplication.translate("MainWindow", "100 %", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistLabel.setText(
            QtGui.QApplication.translate("MainWindow", "Playlist (.m3u)", None, QtGui.QApplication.UnicodeUTF8))
        self.lyricsLabel.setText(
            QtGui.QApplication.translate("MainWindow", "Lyrics (http://www.lyrics.wikia.com)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.totalSongTimeLabel.setText(
            QtGui.QApplication.translate("MainWindow", "00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.curSongTimeLabel.setText(
            QtGui.QApplication.translate("MainWindow", "00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.blackThemeButton.setText(
            QtGui.QApplication.translate("MainWindow", "Black Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.blueThemeButton.setText(
            QtGui.QApplication.translate("MainWindow", "Blue Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.whiteThemeButton.setText(
            QtGui.QApplication.translate("MainWindow", "White Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.pinkThemeButton.setText(
            QtGui.QApplication.translate("MainWindow", "Pink Theme", None, QtGui.QApplication.UnicodeUTF8))


class BlackTheme():
    def blackPlaylistWindowStyle():
        return """
		/*Playlist Window Style*/
			QListView {
				background-color: #000000;
				color: #FFFFFF;
				font-size: 93%;
			}

			QListView::item:selected:!active {
				background-color: #008000;
				color: #FFFFFF;
				font-size: 93%;
			}

			QListView::item:selected:active {
				background-color: #3B9C9C;
				color: #FFFFFF;
				font-size: 93%;
			}

			QListView::item:hover {
				background-color: #6698FF;
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blackLyricsWindowStyle():
        return """
		/*Lyrics Window Style*/
			QTextBrowser {
				background-color: #000000;
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blackMediaButtonsStyle():
        return """
		/*Media Buttons Style*/
			QPushButton {
				background-color: #25383C;
			}

			QPushButton:hover {
				background-color: #504A4B;
			}
		"""

    def blackMainWindowStyle():
        return """
		/*Main Window Style*/
			QMainWindow {
				background-color: #000000;
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blackLabelsStyle():
        return """
		/*Labels Style*/
			QLabel {
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blackThemeButtonsStyle():
        return """
		/*Theme Buttons Style*/
			QPushButton {
				background-color: #FFFFFF;
				color: #000000;
				font-size: 93%;
			}
		"""


class BlueTheme():
    def bluePlaylistWindowStyle():
        return """
		/*Playlist Window Style*/
			QListView {
				background-color: #0000A0;
				color: #FFFFFF;
				font-size: 93%;
			}

			QListView::item:selected:!active {
				background-color: #FFA500;
				color: #000000;
				font-size: 93%;
			}

			QListView::item:selected:active {
				background-color: #FF0000;
				color: #000000;
				font-size: 93%;
			}

			QListView::item:hover {
				background-color: #00FFFF;
				color: #000000;
				font-size: 93%;
			}
		"""

    def blueLyricsWindowStyle():
        return """
		/*Lyrics Window Style*/
			QTextBrowser {
				background-color: #0000A0;
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blueMediaButtonsStyle():
        return """
		/*Media Buttons Style*/
			QPushButton {
				background-color: #000000;
			}

			QPushButton:hover {
				background-color: #25383C;
			}
		"""

    def blueMainWindowStyle():
        return """
		/*Main Window Style*/
			QMainWindow {
				background-color: #2B65EC;
				color: #FFFFFF;
				font-size: 93%;
			}
		"""

    def blueLabelsStyle():
        return """
		/*Labels Style*/
			QLabel {
				color: #00FF00;
				font-size: 93%;
			}
		"""

    def blueThemeButtonsStyle():
        return """
		/*Theme Buttons Style*/
			QPushButton {
				background-color: #FFFFFF;
				color: #000000;
				font-size: 93%;
			}
		"""


class PinkTheme():
    def pinkPlaylistWindowStyle():
        return """
		/*Playlist Window Style*/
			QListView {
				background-color: #C12283;
				color: #000000;
				font-size: 93%;
			}

			QListView::item:selected:!active {
				background-color: #AF7817;
				color: #E5E4E2;
				font-size: 93%;
			}

			QListView::item:selected:active {
				background-color: #C7A317;
				color: #FAEBD7;
				font-size: 93%;
			}

			QListView::item:hover {
				background: #3EA99F;
				color: #FAEBD7;
				font-size: 93%;
			}
		"""

    def pinkLyricsWindowStyle():
        return """
		/*Lyrics Window Style*/
			QTextBrowser {
				background-color: #C12283;
				color: #000000;
				font-size: 93%;
			}
		"""

    def pinkMediaButtonsStyle():
        return """
		/*Media Buttons Style*/
			QPushButton {
				background-color: #79BAEC;
			}

			QPushButton:hover {
				background-color: #56A5EC;
			}
		"""

    def pinkMainWindowStyle():
        return """
		/*Main Window Style*/
			QMainWindow {
				background-color: #F535AA;
				color: #000000;
				font-size: 93%;
			}
		"""

    def pinkLabelsStyle():
        return """
		/*Labels Style*/
			QLabel {
				color: #000000;
				font-size: 93%;
			}
		"""

    def pinkThemeButtonsStyle():
        return """
		/*Theme Buttons Style*/
			QPushButton {
				background-color: #FFFFFF;
				color: #000000;
				font-size: 93%;
			}
		"""


class WhiteTheme():
    def whitePlaylistWindowStyle():
        return """
		/*Playlist Window Style*/
			QListView {
				background-color: None;
				color: None;
				font-size: 93%;
			}

			QListView::item:selected:!active {
				background-color: None;
				color: None;
				font-size: 93%;
			}

			QListView::item:selected:active {
				background-color: None;
				color: None;
				font-size: 93%;
			}

			QListView::item:hover {
				background: None;
				color: None;
				font-size: 93%;
			}
		"""

    def whiteLyricsWindowStyle():
        return """
		/*Lyrics Window Style*/
			QTextBrowser {
				background-color: None;
				color: None;
				font-size: 93%;
			}
		"""

    def whiteMediaButtonsStyle():
        return """
		/*Media Buttons Style*/
			QPushButton {
				background-color: None;
			}

			QPushButton:hover {
				background-color: None;
			}
		"""

    def whiteMainWindowStyle():
        return """
		/*Main Window Style*/
			QMainWindow {
				background-color: None;
				color: None;
				font-size: 93%;
			}
		"""

    def whiteLabelsStyle():
        return """
		/*Labels Style*/
			QLabel {
				color: None;
				font-size: 93%;
			}
		"""

    def whiteThemeButtonsStyle():
        return """
		/*Theme Buttons Style*/
			QPushButton {
				background-color: None;
				color: None;
				font-size: 93%;
			}
		"""



    def __init__(self, parent=None):
        super(MusicPlayer, self).__init__(parent)
        self.setupUi(self)
        pygame.init()
        pygame.mixer.init()
        warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
        self.openFileButton.clicked.connect(self.openFileSelectionDialog)
        self.prevIcon = QtGui.QIcon()
        self.prevIconImage = QtGui.QPixmap("icons/prevButton.png")
        self.prevIcon.addPixmap(self.prevIconImage)
        self.prevSongButton.setIcon(self.prevIcon)
        self.playIcon = QtGui.QIcon()
        self.playIconImage = QtGui.QPixmap("icons/playButton.png")
        self.playIcon.addPixmap(self.playIconImage)
        self.playPauseButton.setIcon(self.playIcon)
        self.pauseIcon = QtGui.QIcon()
        self.pauseIconImage = QtGui.QPixmap("icons/pauseButton.png")
        self.pauseIcon.addPixmap(self.pauseIconImage)
        self.nextIcon = QtGui.QIcon()
        self.nextIconImage = QtGui.QPixmap("icons/nextButton.png")
        self.nextIcon.addPixmap(self.nextIconImage)
        self.nextSongButton.setIcon(self.nextIcon)
        self.volumeSlider.setValue(100)
        self.seekSlider.setValue(0)
        self.prevSongButton.clicked.connect(self.previousSongAudioButton)
        self.playPauseButton.clicked.connect(self.playPauseAudioButton)
        self.nextSongButton.clicked.connect(self.nextSongAudioButton)
        self.previousButtonPressed = False
        self.nextButtonPressed = False
        self.isPlaying = False
        self.volumeSlider.setRange(0, 100)
        self.playlistCurrentSongIndex = 0
        self.playlistModel = QtGui.QStandardItemModel(self.playlistWindow)
        self.playlistWindow.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playlistWindow.doubleClicked.connect(self.playlistItemDoubleClick)
        self.volumeSlider.valueChanged.connect(self.setVolume)
        self.seekSlider.sliderMoved.connect(self.seekMusic)
        self.fileDialogFilePath = ""
        self.lastVisitedDirectory = ""
        self.workingDirectory = os.getcwd()
        self.nextSongTimer = False
        self.songFileToGetLengthFrom = False
        self.songFileLength = 0
        self.timerCounter = 0
        self.nextSongTimer = QTimer()
        self.nextSongTimer.timeout.connect(self.playNextSongInPlaylist)
        self.nextSongTimer.start(1000)
        self.playerWentToFirstSongAutomatically = False
        self.updateSeekTimer = QTimer()
        self.updateSeekTimer.timeout.connect(self.updateSeekSlider)
        self.updateSeekTimer.start(1000)
        self.curVolLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playlistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lyricsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.curSongTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalSongTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.seekSlider.setStyleSheet(self.seekStyle())
        self.volumeSlider.setStyleSheet(self.volumeStyle())
        self.blackThemeButton.clicked.connect(self.switchBlackTheme)
        self.blueThemeButton.clicked.connect(self.switchBlueTheme)
        self.pinkThemeButton.clicked.connect(self.switchPinkTheme)
        self.whiteThemeButton.clicked.connect(self.switchWhiteTheme)
        self.songHasCoverImage = False
        self.putDefaultTheme()
        self.pressCounter = 0
        self.loadSettings()

    def openFileSelectionDialog(self):
        root = tkinter.Tk()
        root.withdraw()
        if self.lastVisitedDirectory != "":
            self.file_path = filedialog.askopenfilename(initialdir=self.lastVisitedDirectory,
                                                        title="Select a song or a playlist", filetypes=(
                ("Media files", "*.mp3 *.m3u"), ("All files", "*.*")))
        else:
            self.file_path = filedialog.askopenfilename(initialdir=self.workingDirectory,
                                                        title="Select a song or a playlist", filetypes=(
                ("Media files", "*.mp3 *.m3u"), ("All files", "*.*")))
        self.playlistCurrentSongIndex = 0
        if self.file_path != "":
            self.fileDialogFilePath = self.file_path
            self.lastVisitedDirectory = os.path.dirname(self.file_path)
            self.saveSettings("LastVisitedDirectory", self.lastVisitedDirectory)
            self.playAudioOnFileSelect(self.fileDialogFilePath)

    def playAudioOnFileSelect(self, path):
        self.timerCounter = 0
        self.seekSlider.setValue(0)
        if path.endswith(".m3u"):
            self.playlist = self.parseM3U(path)
            if pygame.mixer.get_init() != None:
                pygame.mixer.music.stop()
            pygame.mixer.quit()
            if os.path.exists(self.playlist[self.playlistCurrentSongIndex].path):
                self.info = MPEGInfo(open(self.playlist[self.playlistCurrentSongIndex].path, "rb"))
                self.frequency = self.info.sample_rate
                self.channels = self.info.channels
                pygame.mixer.init(frequency=int(self.frequency), channels=int(self.channels))
                self.loadSettings()
                pygame.mixer.music.load(self.playlist[self.playlistCurrentSongIndex].path.encode("utf8"))
                pygame.mixer.music.play()
                self.songFileToGetLengthFrom = MP3(self.playlist[self.playlistCurrentSongIndex].path)
                self.songFileLength = self.songFileToGetLengthFrom.info.length
                self.seekSlider.setRange(0, self.songFileLength)
                self.showSongInfo(self.playlist[self.playlistCurrentSongIndex].path)
                self.addM3USongsToPlaylistWindow()
                self.setCurrentSongHighlighted()
                self.playPauseButton.setIcon(self.pauseIcon)
            else:
                self.playlistModel.removeRows(0, self.playlistModel.rowCount())
                self.lyricsWindow.setText(
                    "The .m3u playlist file you chose appears to be invalid or broken. Please pick another one or play a .mp3 file instead.")
                self.fileDialogFilePath = ""
                self.playPauseButton.setIcon(self.playIcon)
                self.songHasCoverImage = False
                self.loadSettings()
        elif path.endswith(".mp3"):
            if pygame.mixer.get_init() != None:
                pygame.mixer.music.stop()
            pygame.mixer.quit()
            self.info = MPEGInfo(open(path, "rb"))
            self.frequency = self.info.sample_rate
            self.channels = self.info.channels
            pygame.mixer.init(frequency=int(self.frequency), channels=int(self.channels))
            self.loadSettings()
            pygame.mixer.music.load(path.encode("utf8"))
            pygame.mixer.music.play()
            self.songFileToGetLengthFrom = MP3(path)
            self.songFileLength = self.songFileToGetLengthFrom.info.length
            self.seekSlider.setRange(0, self.songFileLength)
            self.showSongInfo(path)
            self.playlistModel.removeRows(0, self.playlistModel.rowCount())
            if self.playlistModel.rowCount() == 0:
                self.songFile = EasyID3(path)
                if "title" in self.songFile:
                    self.songFileTitle = self.songFile["title"][0]
                else:
                    self.songFileTitle = self.fileDialogFilePath.split("/", -1)[-1].split(".mp3")[0]
                self.item = QtGui.QStandardItem("1: " + self.songFileTitle)
                self.playlistModel.appendRow(self.item)
                self.playlistWindow.setModel(self.playlistModel)
                self.setCurrentSongHighlighted()
                self.playPauseButton.setIcon(self.pauseIcon)
        self.playerWentToFirstSongAutomatically = False
        self.isPlaying = True

    def playAudioFromSelectedFile(self, path):
        self.timerCounter = 0
        self.seekSlider.setValue(0)
        if pygame.mixer.get_init() != None:
            pygame.mixer.music.stop()
        # if not self.isMinimized():
        #	pygame.mixer.quit()
        self.info = MPEGInfo(open(path, "rb"))
        self.frequency = self.info.sample_rate
        self.channels = self.info.channels
        pygame.mixer.init(frequency=int(self.frequency), channels=int(self.channels))
        self.loadSettings()
        pygame.mixer.music.load(path.encode("utf8"))
        pygame.mixer.music.play()
        self.songFileToGetLengthFrom = MP3(path)
        self.songFileLength = self.songFileToGetLengthFrom.info.length
        self.seekSlider.setRange(0, self.songFileLength)
        self.showSongInfo(path)
        self.setCurrentSongHighlighted()
        self.playPauseButton.setIcon(self.pauseIcon)
        self.playerWentToFirstSongAutomatically = False
        self.isPlaying = True

    def playNextSongInPlaylist(self):
        if self.fileDialogFilePath.endswith(".m3u"):
            if self.isPlaying == True:
                if os.path.exists(self.playlist[self.playlistCurrentSongIndex].path):
                    self.timerCounter += 1
                    self.songFileToGetLengthFrom = MP3(self.playlist[self.playlistCurrentSongIndex].path)
                    self.songFileLength = self.songFileToGetLengthFrom.info.length
                    if int(self.timerCounter) > int(self.songFileLength):
                        if self.playlistCurrentSongIndex + 1 <= (len(self.playlist) - 1):
                            self.playlistCurrentSongIndex += 1
                            self.playAudioFromSelectedFile(self.playlist[self.playlistCurrentSongIndex].path)
                        elif self.playlistCurrentSongIndex + 1 > (len(self.playlist) - 1):
                            self.playlistCurrentSongIndex = 0
                            self.timerCounter = 0
                            self.seekSlider.setValue(0)
                            if pygame.mixer.get_init() != None:
                                pygame.mixer.music.stop()
                            pygame.mixer.quit()
                            self.info = MPEGInfo(open(self.playlist[self.playlistCurrentSongIndex].path, "rb"))
                            self.frequency = self.info.sample_rate
                            self.channels = self.info.channels
                            pygame.mixer.init(frequency=int(self.frequency), channels=int(self.channels))
                            self.loadSettings()
                            pygame.mixer.music.load(self.playlist[self.playlistCurrentSongIndex].path.encode("utf8"))
                            self.seekSlider.setRange(0, self.songFileLength)
                            self.showSongInfo(self.playlist[self.playlistCurrentSongIndex].path)
                            self.setCurrentSongHighlighted()
                            self.playPauseButton.setIcon(self.playIcon)
                            self.playerWentToFirstSongAutomatically = True
                            self.isPlaying = False
        elif self.fileDialogFilePath.endswith(".mp3"):
            if self.isPlaying == True:
                self.timerCounter += 1
                self.songFileToGetLengthFrom = MP3(self.fileDialogFilePath)
                self.songFileLength = self.songFileToGetLengthFrom.info.length
                if int(self.timerCounter) > int(self.songFileLength):
                    self.timerCounter = 0
                    self.seekSlider.setValue(0)
                    if pygame.mixer.get_init() != None:
                        pygame.mixer.music.stop()
                    pygame.mixer.quit()
                    self.info = MPEGInfo(open(self.fileDialogFilePath, "rb"))
                    self.frequency = self.info.sample_rate
                    self.channels = self.info.channels
                    pygame.mixer.init(frequency=int(self.frequency), channels=int(self.channels))
                    self.loadSettings()
                    pygame.mixer.music.load(self.fileDialogFilePath.encode("utf8"))
                    self.seekSlider.setRange(0, self.songFileLength)
                    self.showSongInfo(self.fileDialogFilePath)
                    self.setCurrentSongHighlighted()
                    self.playPauseButton.setIcon(self.playIcon)
                    self.playerWentToFirstSongAutomatically = True
                    self.isPlaying = False

    def playPauseAudioButton(self):
        if self.fileDialogFilePath.endswith(".m3u") or self.fileDialogFilePath.endswith(".mp3"):
            if self.isPlaying == True:
                if pygame.mixer.get_init() != None:
                    pygame.mixer.music.pause()
                self.playPauseButton.setIcon(self.playIcon)
                self.previousButtonPressed = False
                self.nextButtonPressed = False
                self.isPlaying = False
            elif self.isPlaying == False:
                if self.previousButtonPressed == True or self.nextButtonPressed == True or self.playerWentToFirstSongAutomatically == True:
                    if pygame.mixer.get_init() != None:
                        pygame.mixer.music.play()
                    self.previousButtonPressed = False
                    self.nextButtonPressed = False
                    self.playerWentToFirstSongAutomatically = False
                    self.playPauseButton.setIcon(self.pauseIcon)
                    self.isPlaying = True
                elif self.previousButtonPressed == False or self.nextButtonPressed == False:
                    if pygame.mixer.get_init() != None:
                        pygame.mixer.music.unpause()
                        self.playPauseButton.setIcon(self.pauseIcon)
                        self.isPlaying = True

    def previousSongAudioButton(self):
        if self.fileDialogFilePath.endswith(".m3u") and self.playlistCurrentSongIndex != 0:
            self.pressCounter += 1
            if self.pressCounter == 2:
                self.playlistCurrentSongIndex -= 1
            self.doublePressTimer = QTimer()
            self.doublePressTimer.timeout.connect(self.resetDoublePressPreviousButtonCounter)
            self.doublePressTimer.setSingleShot(True)
            self.doublePressTimer.start(30)
            if os.path.exists(self.playlist[self.playlistCurrentSongIndex].path):
                self.playAudioFromSelectedFile(self.playlist[self.playlistCurrentSongIndex].path)
                self.previousButtonPressed = True
        elif self.fileDialogFilePath.endswith(".m3u") and self.playlistCurrentSongIndex == 0:
            if os.path.exists(self.playlist[self.playlistCurrentSongIndex].path):
                self.playAudioFromSelectedFile(self.playlist[self.playlistCurrentSongIndex].path)
                self.previousButtonPressed = True
        elif self.fileDialogFilePath.endswith(".mp3"):
            self.timerCounter = 0
            self.seekSlider.setValue(0)
            self.songFileToGetLengthFrom = MP3(self.fileDialogFilePath)
            self.songFileLength = self.songFileToGetLengthFrom.info.length
            self.seekSlider.setRange(0, self.songFileLength)
            if self.isPlaying == True:
                if pygame.mixer.get_init() != None:
                    pygame.mixer.music.stop()
                pygame.mixer.music.play()
                self.previousButtonPressed = True
            elif self.isPlaying == False:
                if pygame.mixer.get_init() != None:
                    pygame.mixer.music.stop()
                pygame.mixer.music.load(self.fileDialogFilePath.encode("utf8"))
                self.playPauseButton.setIcon(self.playIcon)
                self.previousButtonPressed = True

    def resetDoublePressPreviousButtonCounter(self):
        self.pressCounter = 0

    def nextSongAudioButton(self):
        if self.fileDialogFilePath.endswith(".m3u"):
            if self.playlistCurrentSongIndex != (len(self.playlist) - 1):
                self.playlistCurrentSongIndex += 1
            elif self.playlistCurrentSongIndex == (len(self.playlist) - 1):
                self.playlistCurrentSongIndex = 0
            if os.path.exists(self.playlist[self.playlistCurrentSongIndex].path):
                self.playAudioFromSelectedFile(self.playlist[self.playlistCurrentSongIndex].path)
                self.nextButtonPressed = True
        elif self.fileDialogFilePath.endswith(".mp3"):
            self.timerCounter = 0
            self.seekSlider.setValue(0)
            self.songFileToGetLengthFrom = MP3(self.fileDialogFilePath)
            self.songFileLength = self.songFileToGetLengthFrom.info.length
            self.seekSlider.setRange(0, self.songFileLength)
            if pygame.mixer.get_init() != None:
                pygame.mixer.music.stop()
            pygame.mixer.music.load(self.fileDialogFilePath.encode("utf8"))
            self.playPauseButton.setIcon(self.playIcon)
            self.isPlaying = False
            self.nextButtonPressed = True

    def showSongInfo(self, path):
        self.filePath = File(path)
        self.audioFrames = self.filePath.tags
        if "APIC:" in self.audioFrames:
            self.artworkFrame = self.audioFrames["APIC:"].data
            with open("icons/albumArt.jpg", "wb") as img:
                img.write(self.artworkFrame)
            self.albumArtCoverImage = "icons/albumArt.jpg"
            self.songHasCoverImage = True
        else:
            self.albumArtCoverImage = self.defaultArtPicture
            self.songHasCoverImage = False
        self.albumArtImage = QImage(self.albumArtCoverImage)
        self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
        self.scene = QGraphicsScene()
        self.scene.addItem(self.pixmapItem)
        self.albumArt.setScene(self.scene)
        self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)
        self.audioFile = EasyID3(path)
        if "title" in self.audioFile:
            self.audioFileTitle = self.audioFile["title"][0]
        else:
            if self.fileDialogFilePath.endswith(".m3u"):
                self.audioFileTitle = \
                self.playlist[self.playlistCurrentSongIndex].path.split("\\", -1)[-1].split(".mp3")[0]
            else:
                self.audioFileTitle = self.fileDialogFilePath.split("/", -1)[-1].split(".mp3")[0]
        self.songName.setText("Song:  " + self.audioFileTitle)
        if "artist" in self.audioFile:
            self.audioFileArtist = self.audioFile["artist"][0]
        else:
            self.audioFileArtist = "Unknown"
        self.artistName.setText("Artist:  " + self.audioFileArtist)
        if "album" in self.audioFile:
            self.audioFileAlbum = self.audioFile["album"][0]
        else:
            self.audioFileAlbum = "Unknown"
        self.albumName.setText("Album: " + self.audioFileAlbum)
        if ("artist" in self.audioFile) and ("title" in self.audioFile):
            try:
                self.lyricsWindow.setText(PyLyrics.getLyrics(self.audioFile["artist"][0], self.audioFile["title"][0]))
            except ValueError:
                self.lyricsWindow.setText("Sorry, no lyrics found for this song and artist combination.")
        else:
            self.lyricsWindow.setText("Sorry, no lyrics found for this song and artist combination.")
        if self.fileDialogFilePath.endswith(".m3u"):
            self.realSongNumber = self.playlistCurrentSongIndex + 1
            self.maxNumberOfSongs = len(self.playlist)
            self.songsCount.setText(str(self.realSongNumber) + " / " + str(self.maxNumberOfSongs))
        else:
            self.songsCount.setText("1 / 1")
        self.songFileToGetLengthFrom = MP3(path)
        self.songFileLength = self.songFileToGetLengthFrom.info.length
        self.totalSongTimeLabel.setText(time.strftime("%M:%S", time.gmtime(self.songFileLength)))

    def addM3USongsToPlaylistWindow(self):
        self.playlistModel.removeRows(0, self.playlistModel.rowCount())
        i = 1
        for track in self.playlist:
            self.playlistSongFile = EasyID3(track.path)
            if "title" in self.playlistSongFile:
                self.playlistSongFileTitle = self.playlistSongFile["title"][0]
            else:
                self.playlistSongFileTitle = track.path.split("\\", -1)[-1].split(".mp3")[0]
            self.item = QtGui.QStandardItem(str(i) + ": " + self.playlistSongFileTitle)
            i += 1
            self.playlistModel.appendRow(self.item)
            self.playlistWindow.setModel(self.playlistModel)

    def playlistItemDoubleClick(self):
        if self.fileDialogFilePath.endswith(".m3u"):
            self.selectedIndexes = self.playlistWindow.selectedIndexes()
            for selected in self.selectedIndexes:
                for track in self.playlist:
                    self.song = EasyID3(track.path)
                    if "title" in self.song:
                        self.songTitle = self.song["title"][0]
                    else:
                        self.songTitle = track.path.split("\\", -1)[-1].split(".mp3")[0]
                    self.selectedSongTitleFromWindow = selected.data().split(": ", 1)[1]
                    if self.songTitle == self.selectedSongTitleFromWindow:
                        self.currentSelectionSongNumber = selected.data().split(": ", 1)[0]
                        self.playlistCurrentSongIndex = int(self.currentSelectionSongNumber) - 1
                        self.playAudioFromSelectedFile(track.path)
                        break
        else:
            self.selectedIndexes = self.playlistWindow.selectedIndexes()
            for selected in self.selectedIndexes:
                self.song = EasyID3(self.fileDialogFilePath)
                if "title" in self.song:
                    self.songTitle = self.song["title"][0]
                else:
                    self.songTitle = self.fileDialogFilePath.split("/", -1)[-1].split(".mp3")[0]
                self.selectedSongTitleFromWindow = selected.data().split(": ", 1)[1]
                if self.songTitle == self.selectedSongTitleFromWindow:
                    self.currentSelectionSongNumber = selected.data().split(": ", 1)[0]
                    self.playlistCurrentSongIndex = int(self.currentSelectionSongNumber) - 1
                    self.playAudioFromSelectedFile(self.fileDialogFilePath)
                    break

    def setCurrentSongHighlighted(self):
        if self.fileDialogFilePath.endswith(".m3u"):
            for i in range(self.playlistModel.rowCount()):
                self.index = self.playlistModel.index(self.playlistCurrentSongIndex, 0, QModelIndex())
                self.selectionModel = self.playlistWindow.selectionModel()
                self.selectionModel.clear()
                self.selectionModel.select(self.index, self.selectionModel.Select)
        else:
            for i in range(self.playlistModel.rowCount()):
                self.index = self.playlistModel.index(0, 0, QModelIndex())
                self.selectionModel = self.playlistWindow.selectionModel()
                self.selectionModel.clear()
                self.selectionModel.select(self.index, self.selectionModel.Select)

    def setVolume(self, value):
        if pygame.mixer.get_init() != None:
            pygame.mixer.music.set_volume(value / 100)
            self.audioLevel = self.volumeSlider.value()
            self.curVolLabel.setText(str(value) + " %")
            self.saveSettings("AudioLevel", value)

    def seekMusic(self, value):
        if pygame.mixer.get_init() != None:
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(value)
            self.timerCounter = value

    def updateSeekSlider(self):
        self.seekSlider.setValue(self.timerCounter)
        self.curSongTimeLabel.setText(time.strftime("%M:%S", time.gmtime(self.timerCounter)))

    def saveSettings(self, setting, value):
        if setting == "LastVisitedDirectory":
            with open("config/LastVisitedDirectory.conf", "w+") as config:
                config.write(str(setting) + " !=! " + str(value))
        elif setting == "AudioLevel":
            with open("config/AudioLevel.conf", "w+") as config:
                config.write(str(setting) + " !=! " + str(value))
        elif setting == "Theme":
            with open("config/Theme.conf", "w+") as config:
                config.write(str(setting) + " !=! " + str(value))

    def loadSettings(self):
        if os.path.isfile("config/LastVisitedDirectory.conf"):
            with open("config/LastVisitedDirectory.conf", "r") as config:
                for line in config:
                    if "LastVisitedDirectory" in line:
                        self.savedLastDir = line.split(" !=! ", 1)[1]
                        if os.path.exists(self.savedLastDir):
                            self.lastVisitedDirectory = self.savedLastDir
                        else:
                            self.lastVisitedDirectory = self.workingDirectory

        if os.path.isfile("config/AudioLevel.conf"):
            with open("config/AudioLevel.conf", "r") as config:
                for line in config:
                    if "AudioLevel" in line:
                        self.savedAudioLevel = line.split(" !=! ", 1)[1]
                        if self.savedAudioLevel != None:
                            self.setVolume(int(self.savedAudioLevel))
                            self.volumeSlider.setValue(int(self.savedAudioLevel))
                        else:
                            self.setVolume(100)
                            self.volumeSlider.setValue(100)

        if os.path.isfile("config/Theme.conf"):
            with open("config/Theme.conf", "r") as config:
                for line in config:
                    if "Theme" in line:
                        self.savedTheme = line.split(" !=! ", 1)[1]
                        if self.savedTheme != None:
                            if self.savedTheme == "Black":
                                self.switchBlackTheme()
                            elif self.savedTheme == "Blue":
                                self.switchBlueTheme()
                            elif self.savedTheme == "Pink":
                                self.switchPinkTheme()
                            elif self.savedTheme == "White":
                                self.switchWhiteTheme()
                        else:
                            self.switchWhiteTheme()

    def parseM3U(self, m3u):
        self.locationOfM3UFile = os.path.dirname(m3u)  # Folder in which the m3u file is located in

        try:
            assert (type(m3u) == "_io.TextIOWrapper")
        except AssertionError:
            m3u = open(m3u, "r")

        line = m3u.readline()
        if not line.startswith("#EXTM3U"):
            return

        playlist = []
        song = Track(None, None, None)

        for line in m3u:
            line = line.strip()
            if line.startswith("#EXTINF:"):
                length, title = line.split("#EXTINF:")[1].split(",", 1)
                song = Track(length, title, None)
            elif len(line) != 0:
                self.songFileName = line.split("\\", -1)[-1]  # Song file name + extention
                self.newPath = self.locationOfM3UFile + "/" + self.songFileName  # The new path to the files (current directory) if the m3u one does not exist
                if os.path.exists(line):
                    song.path = line
                elif os.path.exists(self.newPath):
                    song.path = self.newPath
                else:
                    song.path = ""
                playlist.append(song)
                song = Track(None, None, None)

        m3u.close()

        return playlist

    def switchBlackTheme(self):
        self.playlistWindow.setStyleSheet(BlackTheme.blackPlaylistWindowStyle())
        self.lyricsWindow.setStyleSheet(BlackTheme.blackLyricsWindowStyle())
        self.prevSongButton.setStyleSheet(BlackTheme.blackMediaButtonsStyle())
        self.nextSongButton.setStyleSheet(BlackTheme.blackMediaButtonsStyle())
        self.playPauseButton.setStyleSheet(BlackTheme.blackMediaButtonsStyle())
        self.setStyleSheet(BlackTheme.blackMainWindowStyle())
        self.songName.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.artistName.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.albumName.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.songsCount.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.seekLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.volumeLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.minVolLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.maxVolLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.curVolLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.playlistLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.lyricsLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.totalSongTimeLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.curSongTimeLabel.setStyleSheet(BlackTheme.blackLabelsStyle())
        self.blackThemeButton.setStyleSheet(BlackTheme.blackThemeButtonsStyle())
        self.blueThemeButton.setStyleSheet(BlackTheme.blackThemeButtonsStyle())
        self.whiteThemeButton.setStyleSheet(BlackTheme.blackThemeButtonsStyle())
        self.pinkThemeButton.setStyleSheet(BlackTheme.blackThemeButtonsStyle())
        self.defaultArtPicture = "icons/defaultArtBlack.jpg"
        if self.songHasCoverImage == False:
            self.albumArtImage = QImage(self.defaultArtPicture)
            self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.pixmapItem)
            self.albumArt.setScene(self.scene)
            self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)
        self.saveSettings("Theme", "Black")

    def switchBlueTheme(self):
        self.playlistWindow.setStyleSheet(BlueTheme.bluePlaylistWindowStyle())
        self.lyricsWindow.setStyleSheet(BlueTheme.blueLyricsWindowStyle())
        self.prevSongButton.setStyleSheet(BlueTheme.blueMediaButtonsStyle())
        self.nextSongButton.setStyleSheet(BlueTheme.blueMediaButtonsStyle())
        self.playPauseButton.setStyleSheet(BlueTheme.blueMediaButtonsStyle())
        self.setStyleSheet(BlueTheme.blueMainWindowStyle())
        self.songName.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.artistName.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.albumName.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.songsCount.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.seekLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.volumeLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.minVolLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.maxVolLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.curVolLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.playlistLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.lyricsLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.totalSongTimeLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.curSongTimeLabel.setStyleSheet(BlueTheme.blueLabelsStyle())
        self.blackThemeButton.setStyleSheet(BlueTheme.blueThemeButtonsStyle())
        self.blueThemeButton.setStyleSheet(BlueTheme.blueThemeButtonsStyle())
        self.whiteThemeButton.setStyleSheet(BlueTheme.blueThemeButtonsStyle())
        self.pinkThemeButton.setStyleSheet(BlueTheme.blueThemeButtonsStyle())
        self.defaultArtPicture = "icons/defaultArtBlue.jpg"
        if self.songHasCoverImage == False:
            self.albumArtImage = QImage(self.defaultArtPicture)
            self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.pixmapItem)
            self.albumArt.setScene(self.scene)
            self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)
        self.saveSettings("Theme", "Blue")

    def switchPinkTheme(self):
        self.playlistWindow.setStyleSheet(PinkTheme.pinkPlaylistWindowStyle())
        self.lyricsWindow.setStyleSheet(PinkTheme.pinkLyricsWindowStyle())
        self.prevSongButton.setStyleSheet(PinkTheme.pinkMediaButtonsStyle())
        self.nextSongButton.setStyleSheet(PinkTheme.pinkMediaButtonsStyle())
        self.playPauseButton.setStyleSheet(PinkTheme.pinkMediaButtonsStyle())
        self.setStyleSheet(PinkTheme.pinkMainWindowStyle())
        self.songName.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.artistName.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.albumName.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.songsCount.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.seekLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.volumeLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.minVolLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.maxVolLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.curVolLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.playlistLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.lyricsLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.totalSongTimeLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.curSongTimeLabel.setStyleSheet(PinkTheme.pinkLabelsStyle())
        self.blackThemeButton.setStyleSheet(PinkTheme.pinkThemeButtonsStyle())
        self.blueThemeButton.setStyleSheet(PinkTheme.pinkThemeButtonsStyle())
        self.whiteThemeButton.setStyleSheet(PinkTheme.pinkThemeButtonsStyle())
        self.pinkThemeButton.setStyleSheet(PinkTheme.pinkThemeButtonsStyle())
        self.defaultArtPicture = "icons/defaultArtPink.jpg"
        if self.songHasCoverImage == False:
            self.albumArtImage = QImage(self.defaultArtPicture)
            self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.pixmapItem)
            self.albumArt.setScene(self.scene)
            self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)
        self.saveSettings("Theme", "Pink")

    def switchWhiteTheme(self):
        self.playlistWindow.setStyleSheet(WhiteTheme.whitePlaylistWindowStyle())
        self.lyricsWindow.setStyleSheet(WhiteTheme.whiteLyricsWindowStyle())
        self.prevSongButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.nextSongButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.playPauseButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.setStyleSheet(WhiteTheme.whiteMainWindowStyle())
        self.songName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.artistName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.albumName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.songsCount.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.seekLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.volumeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.minVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.maxVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.curVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.playlistLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.lyricsLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.totalSongTimeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.curSongTimeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.blackThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.blueThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.whiteThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.pinkThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.defaultArtPicture = "icons/defaultArtWhite.jpg"
        if self.songHasCoverImage == False:
            self.albumArtImage = QImage(self.defaultArtPicture)
            self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.pixmapItem)
            self.albumArt.setScene(self.scene)
            self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)
        self.saveSettings("Theme", "White")

    def putDefaultTheme(self):
        self.playlistWindow.setStyleSheet(WhiteTheme.whitePlaylistWindowStyle())
        self.lyricsWindow.setStyleSheet(WhiteTheme.whiteLyricsWindowStyle())
        self.prevSongButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.nextSongButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.playPauseButton.setStyleSheet(WhiteTheme.whiteMediaButtonsStyle())
        self.setStyleSheet(WhiteTheme.whiteMainWindowStyle())
        self.songName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.artistName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.albumName.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.songsCount.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.seekLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.volumeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.minVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.maxVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.curVolLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.playlistLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.lyricsLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.totalSongTimeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.curSongTimeLabel.setStyleSheet(WhiteTheme.whiteLabelsStyle())
        self.blackThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.blueThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.whiteThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.pinkThemeButton.setStyleSheet(WhiteTheme.whiteThemeButtonsStyle())
        self.defaultArtPicture = "icons/defaultArtWhite.jpg"
        if self.songHasCoverImage == False:
            self.albumArtImage = QImage(self.defaultArtPicture)
            self.pixmapItem = QGraphicsPixmapItem(QPixmap.fromImage(self.albumArtImage))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.pixmapItem)
            self.albumArt.setScene(self.scene)
            self.albumArt.fitInView(self.scene.sceneRect(), Qt.IgnoreAspectRatio)

    def seekStyle(self):
        return """
			QSlider::groove:horizontal {
				border: 1px solid #bbb;
				background: white;
				height: 10px;
				border-radius: 4px;
			}

			QSlider::sub-page:horizontal {
				background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
					stop: 0 #66e, stop: 1 #bbf);
				background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
					stop: 0 #bbf, stop: 1 #55f);
				border: 1px solid #777;
				height: 10px;
				border-radius: 4px;
			}

			QSlider::add-page:horizontal {
				background: #fff;
				border: 1px solid #777;
				height: 10px;
				border-radius: 4px;
			}

			QSlider::handle:horizontal {
				background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
					stop:0 #eee, stop:1 #ccc);
				border: 1px solid #777;
				width: 13px;
				margin-top: -2px;
				margin-bottom: -2px;
				border-radius: 4px;
			}

			QSlider::handle:horizontal:hover {
				background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
					stop:0 #fff, stop:1 #ddd);
				border: 1px solid #444;
				border-radius: 4px;
			}

			QSlider::sub-page:horizontal:disabled {
				background: #bbb;
				border-color: #999;
			}

			QSlider::add-page:horizontal:disabled {
				background: #eee;
				border-color: #999;
			}

			QSlider::handle:horizontal:disabled {
				background: #eee;
				border: 1px solid #aaa;
				border-radius: 4px;
			}
		"""

    def volumeStyle(self):
        return """
			QSlider::groove {
				border: 1px solid #999999;
				background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E6E6E6, stop:1 #EEEEEE);
			}

			QSlider::groove:disabled {
				background: #efefef;
			}

			QSlider::handle {
				background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
				border: 1px solid #5c5c5c;
				border-radius: 3px;
				width: 15px;
				height: 15px;
			}

			QSlider::handle:disabled {
				background: #D3D0CD;
			}
		"""


