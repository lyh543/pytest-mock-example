from pytest_mock import MockFixture

from lib.request_manager import request_ten_times, call_ten_times


def test_call_with_mock_function(mocker: MockFixture):
    mocked_func = mocker.Mock()
    call_ten_times(mocked_func)

    mocked_func.assert_has_calls([
        mocker.call(index) for index in range(10)
    ])

def test_call_with_mock_object(mocker: MockFixture):
    mocked_request = mocker.Mock()
    request_ten_times(mocked_request)

    mocked_request.assert_has_calls([
        mocker.call.get(index) for index in range(10)
    ])

