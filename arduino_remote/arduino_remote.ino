#include <IRLibAll.h>

IRsend mySender;

void setup() {
  Serial.begin(9600);
}

void loop() {
  char c = Serial.read();
  if (c != -1) {
    switch (c) {
      case 'm':
        mySender.send(NEC,0x4BB6906F, 32);  // TV/CD
        break;
      case 'r':
        mySender.send(NEC,0x4B36D32C, 32);  // on-off
        break;
      case 't':
        mySender.send(NEC,0x4B3631CE, 32);  // BD/DVD
        break;
       case 'l':
        mySender.send(NEC,0x4BB6B04F, 32);  // game
        break;
       case 'q':
        mySender.send(NEC,0x4BB640BF, 32); // vol +
        break;
       case 'w':
        mySender.send(NEC,0x4BB6C03F, 32); // vol -
        break;
       case 'a':
        mySender.send(NEC,0x4BB6F906, 32); // aux
        break;
    }
    Serial.write(c);
  }
}
