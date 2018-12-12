#!/usr/local/bin/python3

# https://www.lintcode.com/problem/toy-factory/description?_from=ladder&&fromId=8
# Example
# 工厂模式是一种常见的设计模式。请实现一个玩具工厂 ToyFactory 用来产生不同的玩具类。可以假设只有猫和狗两种玩具。
#
# 样例
# ToyFactory tf = ToyFactory();
# Toy toy = tf.getToy('Dog');
# toy.talk();
# >> Wow
#
# toy = tf.getToy('Cat');
# toy.talk();
# >> Meow

"""
Solution:

Corner cases:
"""


"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print("Wow")

class Cat(Toy):
    # Write your code here
    def talk(self):
        print("Meow")

class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        # Write your code here
        toy = None
        if type == "Cat":
            toy = Cat()
        elif type == "Dog":
            toy = Dog()
        else:
            print("type not handled error: " + type)
        return toy


/**
 * Your object will be instantiated and called as such:
 * ToyFactory* tf = new ToyFactory();
 * Toy* toy = tf->getToy(type);
 * toy->talk();
 */
class Toy {
public:
    virtual void talk() const=0;
};

class Dog: public Toy {
    // Write your code here
    // Note: be careful to use const
    void talk() const {
        cout << "Wow" << endl;
    }
};

class Cat: public Toy {
    // Write your code here
    void talk() const {
        cout << "Meow" << endl;
    }
};

class ToyFactory {
public:
    /**
     * @param type a string
     * @return Get object of the type
     */
    Toy* getToy(string& type) {
        // Write your code here
        if (type == "Dog") {
            return new Dog();
        }
        if (type == "Cat") {
            return new Cat();
        }
        return NULL;

    }
};

# Test Cases
if __name__ == "__main__":
    solution = Solution()
