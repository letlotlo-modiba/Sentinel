from simulator.utils import generate_ip, now

def test_generate_ip_format():
    ip = generate_ip()
    parts = ip.split(".")

    assert len(parts) == 4
    assert all(0 <= int(p) <= 255 for p in parts)

def test_now_returns_string():
    t = now()

    assert isinstance(t, str)