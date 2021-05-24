
from example1 import *

class Tests:

  def test_foo(self):
    """
    Test the foo method with variety of args
    """
    assert foo("Hello", "world!") == "Hello world!"
    assert foo("Hello", "") == "Hello "
    assert foo("world!", "Hello") == "world! Hello"

  def test_bar(self):
    """
    Test the bar method returns the proper text
    """
    assert type(bar()) == str
    assert bar() == "Hello world!"
  
  def test_baz(self, capsys):
    """
    Test the baz method prints the proper text
    """
    baz()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!\n"

  def test_main(self, capsys):
    """
    Test the main method
    """
    main()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!\nHello world!\nHello world!\n"
