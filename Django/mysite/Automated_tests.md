# Introducing automated testing
What are automated tests?
Tests are routines that check the operation of your code.
Testing operates at different levels. Some tests might apply to a tiny detail (does a particular model method return
values as expected?) while others examine the overall operation of the software (does a sequence of user inputs on the
site produce the desired result?). That’s no different from the kind of testing you did earlier in Tutorial 2, using the
shell to examine the behavior of a method, or running the application and entering data to check how it behaves.
What’s different in automated tests is that the testing work is done for you by the system. You create a set of tests
once, and then as you make changes to your app, you can check that your code still works as you originally intended,
without having to perform time consuming manual testing.
# Why you need to create tests
So why create tests, and why now?
You may feel that you have quite enough on your plate just learning Python/Django, and having yet another thing
to learn and do may seem overwhelming and perhaps unnecessary. After all, our polls application is working quite
happily now; going through the trouble of creating automated tests is not going to make it work any better. If creating
the polls application is the last bit of Django programming you will ever do, then true, you don’t need to know how to
create automated tests. But, if that’s not the case, now is an excellent time to learn.
# Tests will save you time
Up to a certain point, ‘checking that it seems to work’ will be a satisfactory test. In a more sophisticated application,
you might have dozens of complex interactions between components.
A change in any of those components could have unexpected consequences on the application’s behavior. Checking
that it still ‘seems to work’ could mean running through your code’s functionality with twenty different variations of
your test data to make sure you haven’t broken something - not a good use of your time.
That’s especially true when automated tests could do this for you in seconds. If something’s gone wrong, tests will
also assist in identifying the code that’s causing the unexpected behavior.
Sometimes it may seem a chore to tear yourself away from your productive, creative programming work to face the
unglamorous and unexciting business of writing tests, particularly when you know your code is working properly.
However, the task of writing tests is a lot more fulfilling than spending hours testing your application manually or
trying to identify the cause of a newly-introduced problem.
# Tests don’t just identify problems, they prevent them
It’s a mistake to think of tests merely as a negative aspect of development.
Without tests, the purpose or intended behavior of an application might be rather opaque. Even when it’s your own
code, you will sometimes find yourself poking around in it trying to find out what exactly it’s doing.
Tests change that; they light up your code from the inside, and when something goes wrong, they focus light on the
part that has gone wrong - even if you hadn’t even realized it had gone wrong.
Tests make your code more attractive
You might have created a brilliant piece of software, but you will find that many other developers will refuse to look
at it because it lacks tests; without tests, they won’t trust it. Jacob Kaplan-Moss, one of Django’s original developers,
says “Code without tests is broken by design.”
That other developers want to see tests in your software before they take it seriously is yet another reason for you to
start writing tests.

# Tests help teams work together
The previous points are written from the point of view of a single developer maintaining an application. Complex
applications will be maintained by teams. Tests guarantee that colleagues don’t inadvertently break your code (and
that you don’t break theirs without knowing). If you want to make a living as a Django programmer, you must be good
at writing tests!

# Basic testing strategies
There are many ways to approach writing tests.
Some programmers follow a discipline called “test-driven development”; they actually write their tests before they
write their code. This might seem counter-intuitive, but in fact it’s similar to what most people will often do anyway:
they describe a problem, then create some code to solve it. Test-driven development formalizes the problem in a
Python test case.
More often, a newcomer to testing will create some code and later decide that it should have some tests. Perhaps it
would have been better to write some tests earlier, but it’s never too late to get started.
Sometimes it’s difficult to figure out where to get started with writing tests. If you have written several thousand lines
of Python, choosing something to test might not be easy. In such a case, it’s fruitful to write your first test the next
time you make a change, either when you add a new feature or fix a bug.
So let’s do that right away.
