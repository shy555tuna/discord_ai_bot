#!/usr/bin/env bash
set -e

VENV_DIR=".venv"
PYTHON=""

echo ""
echo "╔══════════════════════════════════════╗"
echo "║        ShyNet — AI Discord Bot       ║"
echo "╚══════════════════════════════════════╝"
echo ""

find_python() {
  for cmd in python3.12 python3.11 python3 python; do
    if command -v "$cmd" &>/dev/null; then
      version=$("$cmd" -c "import sys; print(sys.version_info[:2])" 2>/dev/null)
      major=$("$cmd" -c "import sys; print(sys.version_info.major)" 2>/dev/null)
      minor=$("$cmd" -c "import sys; print(sys.version_info.minor)" 2>/dev/null)
      if [ "$major" -ge 3 ] && [ "$minor" -ge 11 ]; then
        PYTHON="$cmd"
        echo "✓ Found Python $major.$minor at $(which $cmd)"
        return 0
      fi
    fi
  done
  return 1
}

if ! find_python; then
  echo "✗ Python 3.11+ is required but not found."
  echo ""
  echo "  macOS:  brew install python@3.11"
  echo "  Ubuntu: sudo apt install python3.11 python3.11-venv"
  echo "  Other:  https://www.python.org/downloads/"
  exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
  echo ""
  echo "→ Creating virtual environment..."
  "$PYTHON" -m venv "$VENV_DIR"
  echo "✓ Virtual environment created"
fi

source "$VENV_DIR/bin/activate"
echo "✓ Virtual environment activated"

echo ""
echo "→ Installing dependencies..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo "✓ Dependencies installed"

OS_TYPE="$(uname -s 2>/dev/null || echo Unknown)"
if [ "$OS_TYPE" = "Darwin" ]; then
  echo ""
  echo "→ Applying macOS SSL certificate fix..."
  CERT_FILE=$(python -c "import certifi; print(certifi.where())")
  export SSL_CERT_FILE="$CERT_FILE"
  export REQUESTS_CA_BUNDLE="$CERT_FILE"

  PY_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  CERT_CMD="/Applications/Python ${PY_VERSION}/Install Certificates.command"
  if [ -f "$CERT_CMD" ]; then
    bash "$CERT_CMD" &>/dev/null || true
  fi
  echo "✓ SSL certificates configured"
fi

echo ""
echo "✓ Starting ShyNet at http://localhost:5000"
echo "  Press Ctrl+C to stop"
echo ""

if [ "$OS_TYPE" = "Darwin" ]; then
  (sleep 1.5 && open http://localhost:5000) &
elif command -v xdg-open &>/dev/null; then
  (sleep 1.5 && xdg-open http://localhost:5000) &
fi

python app.py
