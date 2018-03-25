import ast
from flake8_inline_requests import InlineRequestsChecker
from flake8_inline_requests import InlineRequestsFinder


def run_checker(code):
    tree = ast.parse(code)
    checker = InlineRequestsChecker(tree, None)
    return list(checker.run())


def test_pass_with_meta_httpstatus_true():
    code = "resp = yield Request('http://x.com', meta={'handle_httpstatus_all': True})"
    errors = run_checker(code)
    assert len(errors) == 0


def test_pass_with_meta_httpstatus_eval_as_true():
    code = "resp = yield Request('http://x.com', meta={'handle_httpstatus_all': 1})"
    errors = run_checker(code)
    assert len(errors) == 0


def test_fail_missing_meta():
    code = "resp = yield Request('http://x.com')"
    lineno, colno, msg, cls = run_checker(code)[0]
    assert lineno == 1
    assert colno == 13
    assert msg == InlineRequestsFinder.MSG


def test_fail_with_meta_missing_httpstatus():
    code = "resp = yield Request('http://x.com', meta={'item': 1})"
    lineno, colno, msg, cls = run_checker(code)[0]
    assert lineno == 1
    assert colno == 13
    assert msg == InlineRequestsFinder.MSG


def test_fail_with_meta_httpstatus_false():
    code = "resp = yield Request('http://x.com', meta={'handle_httpstatus_all': False})"
    lineno, colno, msg, cls = run_checker(code)[0]
    assert lineno == 1
    assert colno == 13
    assert msg == InlineRequestsFinder.MSG


def test_fail_with_form_request():
    code = "resp = yield FormRequest('http://x.com')"
    lineno, colno, msg, cls = run_checker(code)[0]
    assert lineno == 1
    assert colno == 13
    assert msg == InlineRequestsFinder.MSG
