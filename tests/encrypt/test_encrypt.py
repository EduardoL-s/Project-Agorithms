from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('testando', 2) == 'odnats_et'

    assert encrypt_message('testando', 3) == 'set_odnat'

    assert encrypt_message('testando', 10) == 'odnatset'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('testando', 'dois')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(['testando'], 2)
