from pytest import mark


@mark.skip(reason="broken by deploy somenumber")
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

@mark.skip(reason="Not a staging environment")
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'

@mark.xfail(reason="Env was not QA")
def test_this_should_always_pass(app_config):
    assert True

@mark.xfail(reason="this feature should have been deprecated")
def test_this_should_always_fail(app_config):
    assert False


@mark.skip
def test_this_needs_work(app_config):
    assert False


