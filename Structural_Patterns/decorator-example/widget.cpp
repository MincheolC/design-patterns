#include <iostream>

using namespace std;

/* Component (interface) */
class Widget {

public:
  virtual void draw() = 0;
  virtual ~Widget() {}
};

/* ConcreteComponent */
class TextField : public Widget {

private:
   int width, height;

public:
   TextField( int w, int h ){
      width  = w;
      height = h;
   }

   void draw() {
      cout << "TextField: " << width << ", " << height << '\n';
   }
};

/* Decorator (interface) */
class Decorator : public Widget {

private:
   Widget* wid;       // reference to Widget

public:
   Decorator( Widget* w )  {
     wid = w;
   }

   void draw() {
     wid->draw();
   }

   ~Decorator() {
     delete wid;
   }
};

/* ConcreteDecoratorA */
class BorderDecorator : public Decorator {

public:
   BorderDecorator( Widget* w ) : Decorator( w ) { }
   void draw() {
      Decorator::draw();
      cout << "   BorderDecorator" << '\n';
   }
};

/* ConcreteDecoratorB */
class ScrollDecorator : public Decorator {
public:
   ScrollDecorator( Widget* w ) : Decorator( w ) { }
   void draw() {
      Decorator::draw();
      cout << "   ScrollDecorator" << '\n';
   }
};

int main( void ) {

   Widget* aWidget = new BorderDecorator(
                     new ScrollDecorator(
                     new TextField( 80, 24 )));
   aWidget->draw();
   delete aWidget;
}