from src.decorators import log


def test_decorator(capsys):

    @log()
    def summ(x, y):
        return x + y

    (summ(1, 2))
    capture = capsys.readouterr()
    log_output = capture.out + capture.err
    assert log_output == "summ  ok\n"


def test_decorator_err(capsys):
    @log()
    def zero_div(x):
        return x / 0

    try:
        zero_div(10)
        capture = capsys.readouterr()
        log_out = capture.out + capture.err
    except ZeroDivisionError:
        capture = capsys.readouterr()
        log_out = capture.out + capture.err
        assert log_out == f"zero_div error: ZeroDivisionError. Inputs {(10,)}, {{}}\n"
