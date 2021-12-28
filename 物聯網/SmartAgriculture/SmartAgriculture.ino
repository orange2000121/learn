#include <SD.h>

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
// #include <Fonts/FreeSerif12pt7b.h>
// #include <Fonts/FreeSansBold9pt7b.h>
// #include <Fonts/FreeSans9pt7b.h>
#include <SPI.h>

#include "DHT.h"

//dht11
#define dhtPin 2           //讀取DHT11 Data
#define dhtType DHT11      //選用DHT11
DHT dht(dhtPin, dhtType);  // Initialize DHT sensor


//土壤濕度
const int sensorPin = 1;


//光敏電阻
#define lightPin 0

//螢幕
#define TFT_CS 5   // TFT LCD的CS PIN腳
#define TFT_DC 4   // TFT DC(A0、RS)
#define TFT_RST 3  // TFT Reset
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);


void setup() {
  Serial.begin(115200);
  pinMode(TFT_CS, OUTPUT);
  digitalWrite(TFT_CS, HIGH);
 
  // 初始設定 ST7735S TFT LCD
  tft.initR(INITR_BLACKTAB);
  tft.fillScreen(ST77XX_BLUE);

  Serial.print("Initializing SD card...");
  if (!SD.begin()) {
    Serial.println("failed!");
    while(1);  // stay here
  }
  Serial.println("OK!");
 
  File root = SD.open("/");  // 開啟SD card 根目錄
  printDirectory(root, 0);   // 列出所有檔案名稱跟檔案大小
  root.close();              // 關閉開啟的檔案
}

void showIcons() {
  tft.fillRoundRect(30, 95, 30, 30, 5, ST77XX_MAGENTA);  //圓角矩形x,y,w,h,radius,color
  tft.fillCircle(80, 110, 15, ST77XX_BLUE);              //圓形 x,y,radius
  tft.drawRect(105, 95, 30, 30, ST77XX_GREEN);           //矩形外框 x,y,width,height
  delay(500);
}

int measuringSoil() {
  //土壤溼度感測
  int moist;
  int Dmoist;
  moist = analogRead(sensorPin);
  Dmoist = digitalRead(sensorPin);
  Serial.print("類比數值 : ");
  Serial.println(moist);
  Serial.println("\n");
  Serial.print("數位數值 : ");
  Serial.println(Dmoist);
  Serial.println("\n");
  return moist, Dmoist;
}

int measuringLight() {
  int light = analogRead(lightPin);
  Serial.print("light : ");
  Serial.println(light);
  Serial.println("\n");
  return light;
}

int measuringHumidityandTemperature(){
  //dht11 空氣溫溼度感測器
  float h = dht.readHumidity();         //讀取濕度
  float t = dht.readTemperature();      //讀取攝氏溫度
  // float f = dht.readTemperature(true);  //讀取華氏溫度
  if (isnan(h) || isnan(t)) {
    Serial.println("無法從DHT傳感器讀取！");
    return;
  }
  Serial.print("濕度: ");
  Serial.print(h);
  Serial.print("%\t");
  Serial.print("攝氏溫度: ");
  Serial.print(t);
  Serial.print("*C\t");
  // Serial.print("華氏溫度: ");
  // Serial.print(f);
  // Serial.print("*F\n");
  return h,t;
}
void loop() {
  int moist;
  int Dmoist;
  moist,Dmoist= measuringSoil();
  //光敏電阻
  int light=measuringLight();
  // dht11
  float h,t;
  h,t=measuringHumidityandTemperature();
  

  //判斷環境
  int EnvironmentalQuality = 0;
  if (18 <= t && t <= 30) {
    EnvironmentalQuality++;
  }
  if (h > 50) {
    EnvironmentalQuality++;
  }
  if (light > 1) {
    EnvironmentalQuality++;
  }
  if(moist>500){
    EnvironmentalQuality++;
  }
  if (EnvironmentalQuality >= 2) {
    Serial.println("Excellent");
    bmpDraw("happy.bmp", 0, 0);
  } else if (EnvironmentalQuality >= 1) {
    Serial.println("good");
    bmpDraw("nomal.bmp", 0, 0);
  } else {
    Serial.println("bad");
    bmpDraw("sad.bmp", 0, 0);
  }
  delay(5000);
}
// 以下程式將讀取Bitmap檔案，並顯示在LCD，給予緩衝20 Pixel 
#define BUFFPIXEL 20
 
void bmpDraw(char *filename, uint8_t x, uint16_t y) {
 
  File     bmpFile;
  int      bmpWidth, bmpHeight;   // W+H in pixels
  uint8_t  bmpDepth;              // Bit depth (currently must be 24)
  uint32_t bmpImageoffset;        // Start of image data in file
  uint32_t rowSize;               // Not always = bmpWidth; may have padding
  uint8_t  sdbuffer[3*BUFFPIXEL]; // pixel buffer (R+G+B per pixel)
  uint8_t  buffidx = sizeof(sdbuffer); // Current position in sdbuffer
  boolean  goodBmp = false;       // Set to true on valid header parse
  boolean  flip    = true;        // BMP is stored bottom-to-top
  int      w, h, row, col;
  uint8_t  r, g, b;
  uint32_t pos = 0, startTime = millis();
 
  if((x >= tft.width()) || (y >= tft.height())) return;
 
  Serial.println();
  Serial.print(F("Loading image '"));
  Serial.print(filename);
  Serial.println('\'');
 
  // Open requested file on SD card
  if ((bmpFile = SD.open(filename)) == NULL) {
    Serial.print(F("File not found"));
    return;
  }
 
  // Parse BMP header
  if(read16(bmpFile) == 0x4D42) { // BMP signature
    Serial.print(F("File size: ")); Serial.println(read32(bmpFile));
    (void)read32(bmpFile); // Read & ignore creator bytes
    bmpImageoffset = read32(bmpFile); // Start of image data
    Serial.print(F("Image Offset: ")); Serial.println(bmpImageoffset, DEC);
    // Read DIB header
    Serial.print(F("Header size: ")); Serial.println(read32(bmpFile));
    bmpWidth  = read32(bmpFile);
    bmpHeight = read32(bmpFile);
    if(read16(bmpFile) == 1) { // # planes -- must be '1'
      bmpDepth = read16(bmpFile); // bits per pixel
      Serial.print(F("Bit Depth: ")); Serial.println(bmpDepth);
      Serial.print(F("read32(bmpFile): ")); Serial.println(read32(bmpFile));
      if((bmpDepth == 24) && (read32(bmpFile) == 0)) { // 0 = uncompressed
 
        goodBmp = true; // Supported BMP format -- proceed!
        Serial.print(F("Image size: "));
        Serial.print(bmpWidth);
        Serial.print('x');
        Serial.println(bmpHeight);
 
        // BMP rows are padded (if needed) to 4-byte boundary
        rowSize = (bmpWidth * 3 + 3) & ~3;
 
        // If bmpHeight is negative, image is in top-down order.
        // This is not canon but has been observed in the wild.
        if(bmpHeight < 0) {
          bmpHeight = -bmpHeight;
          flip      = false;
        }
 
        // Crop area to be loaded
        w = bmpWidth;
        h = bmpHeight;
        if((x+w-1) >= tft.width())  w = tft.width()  - x;
        if((y+h-1) >= tft.height()) h = tft.height() - y;
 
        // Set TFT address window to clipped image bounds
        tft.startWrite();
        tft.setAddrWindow(x, y, w, h);
 
        for (row=0; row<h; row++) { // For each scanline...
           if(flip) // Bitmap is stored bottom-to-top order (normal BMP)
            pos = bmpImageoffset + (bmpHeight - 1 - row) * rowSize;
          else     // Bitmap is stored top-to-bottom
            pos = bmpImageoffset + row * rowSize;
          if(bmpFile.position() != pos) { // Need seek?
            tft.endWrite();
            bmpFile.seek(pos);
            buffidx = sizeof(sdbuffer); // Force buffer reload
          }
 
          for (col=0; col<w; col++) { // For each pixel...
            // Time to read more pixel data?
            if (buffidx >= sizeof(sdbuffer)) { // Indeed
              bmpFile.read(sdbuffer, sizeof(sdbuffer));
              buffidx = 0; // Set index to beginning
              tft.startWrite();
            }
 
            // Convert pixel from BMP to TFT format, push to display
            b = sdbuffer[buffidx++];
            g = sdbuffer[buffidx++];
            r = sdbuffer[buffidx++];
            tft.pushColor(tft.color565(r,g,b));
          } // end pixel
        } // end scanline
        tft.endWrite();
        Serial.print(F("Loaded in "));
        Serial.print(millis() - startTime);
        Serial.println(" ms");
      } // end goodBmp
    }
  }
 
  bmpFile.close();
  if(!goodBmp) Serial.println(F("BMP format not recognized."));
}
 
uint16_t read16(File f) {
  uint16_t result;
  ((uint8_t *)&result)[0] = f.read(); // LSB
  ((uint8_t *)&result)[1] = f.read(); // MSB
  return result;
}
 
uint32_t read32(File f) {
  uint32_t result;
  ((uint8_t *)&result)[0] = f.read(); // LSB
  ((uint8_t *)&result)[1] = f.read();
  ((uint8_t *)&result)[2] = f.read();
  ((uint8_t *)&result)[3] = f.read(); // MSB
  return result;
}
void printDirectory(File dir, int numTabs) {
  while (true) {
 
    File entry =  dir.openNextFile();
    if (! entry) {
      // no more files
      break;
    }
    for (uint8_t i = 0; i < numTabs; i++) {
      Serial.print('\t');
    }
    Serial.print(entry.name());
    if (entry.isDirectory()) {
      Serial.println("/");
      printDirectory(entry, numTabs + 1);
    } else {
      // files have sizes, directories do not
      Serial.print("\t\t");
      Serial.println(entry.size(), DEC);
    }
    entry.close();
  }
}
