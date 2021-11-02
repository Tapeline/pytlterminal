# pytlterminal

Simple library for creating command line apps.

## Usage:
`term = Terminal(prefix)` - create Terminal instance. Prefix will be used for output
`@term.cmd("command")` - registers decorated function as command executor. You can stack them.
`term.out|err|warn|info(msg)` - outputs `msg` with different prefix
`term.stop([reason])` - stop the terminal
`term.run()` - run the terminal

Example:
```
import terminal
term = terminal.Terminal("example")


@term.cmd("quit") # will run on quit, quit app, quit ...
def quit_terminal(cmd): # the full command will be casted to first argument
  term.info("Bye!")
  term.stop("Ended by user.")
  

term.run()
```
The console:
```
example>quit
(i) Bye!
example console was ended. Reason: ended by user
```
