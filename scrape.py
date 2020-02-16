def poster_call():
    poster_path = "C:/Users/dev29/PycharmProjects/Music/Art/artist.png"
    artist_name = 'Lauv'
    url = 'https://en.wikipedia.org/wiki/'+artist_name
    try:
        open_url = requests.get(url)
    except:
        pass
    soup = bs4.BeautifulSoup(open_url.content, 'html.parser')
    image = soup.find_all('img')
    print(image)
    image_link = image[0].get('src', '')
    print('https:'+image_link)
    poster = requests.get('https:'+image_link)
    with open(poster_path, 'wb') as img_handle:
        img_handle.write(poster.content)

poster_call()

track = MP3(filename_path)
tags = ID3(filename_path)
print("ID3 tags included in this song ------------------")
print(tags.pprint())
print("-------------------------------------------------")
pict = tags.get("APIC:").data
im = Image.open(BytesIO(pict))
print('Picture size : ' + str(im.size))

photo = ImageTk.PhotoImage(Image.open('Art/art.png'))
labelphoto = Label(root, image = photo)
labelphoto.pack()
labelphoto.place(x=20,y=10)

track = MP3(filename_path)
tags = ID3(filename_path)
print("ID3 tags included in this song ------------------")
print(tags.pprint())
print("-------------------------------------------------")
pict = tags["APIC:"].data
im = Image.open(BytesIO(pict))
print('Picture size : ' + str(im.size))
with open("Art/art.png", "wb") as img:
    img.write(tags)
atags = "Art/albumArt.png"
photo = ImageTk.PhotoImage(Image.open('Art/art.png'))
labelphoto = Label(root, image=photo)
labelphoto.pack()
labelphoto.place(x=20, y=10)


def showSongInfo(self, filename_path):
    self.filePath = File(filename_path)
    self.audioFrames = self.filePath.tags
    if "APIC:" in self.audioFrames:
        self.artworkFrame = self.audioFrames["APIC:"].data
        with open("C:/Users/dev29/PycharmProjects/Music/Art/albumArt.jpg", "wb") as img:
            img.write(self.artworkFrame)
        self.albumArtCoverImage = "C:/Users/dev29/PycharmProjects/Music/Art/albumArt.jpg"
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

def showSongInfo(filename_path):
    filePath = filename_path
    audioFrames = ID3(filename_path)
    artworkFrame = audioFrames["APIC:"].data
    with open("C:/Users/dev29/PycharmProjects/Music/Art/albumArt.jpg", "wb") as img:
        img.write(artworkFrame)
    albumArtCoverImage = "C:/Users/dev29/PycharmProjects/Music/Art/albumArt.jpg"