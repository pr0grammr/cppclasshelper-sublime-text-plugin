#include <iostream>

namespace {
    int a = 10;
};

namespace OS
{
    class Window : public Component
    {
        public:

        void close();
        void open();

        inline void init()
        {
            std::cout << "test";
        }

        static int getSize();

    };
};