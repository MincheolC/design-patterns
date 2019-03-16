class Image {
  display() {}
}

class RealImage extends Image {
  constructor(fileName) {
    super();
    this.fileName = fileName;
    this.loadFromDisk(fileName);
  }

  display() {
    console.log(`Displaying ${this.fileName}`);
  }

  loadFromDisk(fileName) {
    console.log(`Loading ${fileName}`);
  }
}

class ProxyImage extends Image {
  constructor(fileName) {
    super();
    this.fileName = fileName;
  }

  display() {
    if (!this.realImage) {
      this.realImage = new RealImage(this.fileName);
    }
    this.realImage.display();
  }
}

// run
const image = new ProxyImage('test_image.png');
// load from disk
image.display();
// not load from disk
image.display();
