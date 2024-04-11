```python
from main import enhanced_calculator

def test_enhanced_calculator_log_operation():
    assert enhanced_calculator(1, 0, 'log') == 0, "Log(1) should be 0"
    assert enhanced_calculator(10, 1, 'log') == 1, "Log_10(10) should be 1"
    assert enhanced_calculator(100, 2, 'log') == 2, "Log_100(100) should be 2"
    assert enhanced_calculator(16, 4, 'log') == 0.5, "Log_4(16) should be 0.5"
```