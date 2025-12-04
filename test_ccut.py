"""Tests for ccut command"""
import subprocess

def run_ccut(args):
    """Helper function to run ccwc command with given arguments

    Args:
        args: list of command-line arguments

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['ccut'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_split_tsv():
    """Test the output of a tsv file using ccut"""
    print("Testing: the output of a tsv file using ccut")
    stdout, stderr, returncode = run_ccut(['sample.tsv', '-f1,2'])

    print(f"  Output: {stdout}")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Test failed with errors : {stderr}"
    
    first_line = stdout.strip().split("\n")[0]
    # Check if each line is split by tabulation
    assert "\t" in first_line,  "Each line must be split by tabulation"

    # Check if each line contains exactly 2 members
    assert len(first_line.split()) == 2, f"Each line of the output must contain exactly 2 fields, got {len(first_line.split())}"

    print("  ✓ Test passed!")


def main():
    print("=" * 50)
    print("Testing ccut - Byte Count Feature")
    print("=" * 50)

    try:
        test_split_tsv()
        print("\n✓ All tests passed!")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()