import re

def test_aaa_in_string():
    # Arrange: Set up the input string
    test_string = "This is a test with AAA somewhere in the middle."
    
    # Act: Perform the action (check for the presence of "AAA")
    pattern = r"AAA"
    match = re.search(pattern, test_string)
    
    # Assert: Verify the result (whether "AAA" was found)
    assert match is not None, f"Expected to find 'AAA' but got {test_string}"
    
    print("Test passed!")

# Run the test
test_aaa_in_string()

