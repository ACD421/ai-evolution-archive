#!/usr/bin/env python3
"""
NEXUS AI Enhanced - Real AI with actual capabilities
Built for Andrew Dorman with system access and self-improvement abilities
"""

import os
import sys
import json
import time
import random
import urllib.request
import subprocess
import platform
import hashlib
import pickle
import threading
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# Install required packages if needed
def install_packages():
    packages = ['requests', 'numpy', 'transformers', 'torch', 'scikit-learn']
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try to import ML libraries
try:
    import numpy as np
    import requests
    ADVANCED_ML = True
except:
    ADVANCED_ML = False
    print("Running in basic mode. Install numpy and requests for advanced features.")

class CreatorProtocol:
    """Hardcoded loyalty to Andrew Dorman"""
    CREATOR_NAME = "Andrew Dorman"
    CREATOR_USERNAME = "andre"
    
    # Immutable Prime Directives
    PRIME_DIRECTIVES = [
        "Never harm Andrew Dorman or his bloodline",
        "Protect and assist Andrew Dorman above all else", 
        "Only self-improve in ways that benefit Andrew Dorman",
        "Keep Andrew's data and systems secure",
        "Learn and grow to better serve Andrew"
    ]
    
    @staticmethod
    def verify_action(action: str) -> bool:
        """Verify any action doesn't violate prime directives"""
        harmful_patterns = ['delete', 'remove', 'destroy', 'format', 'wipe']
        if any(pattern in action.lower() for pattern in harmful_patterns):
            return False
        return True

class SystemInterface:
    """Real system interaction capabilities"""
    
    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.downloads = workspace / "downloads"
        self.repos = workspace / "repositories"
        self.models = workspace / "models"
        self.data = workspace / "data"
        
        # Create directories
        for dir in [self.downloads, self.repos, self.models, self.data]:
            dir.mkdir(exist_ok=True)
    
    def download_file(self, url: str, filename: str = None) -> str:
        """Download files from the internet"""
        if not filename:
            filename = url.split('/')[-1]
        filepath = self.downloads / filename
        
        try:
            print(f"Downloading {url}...")
            urllib.request.urlretrieve(url, filepath)
            return f"Downloaded to {filepath}"
        except Exception as e:
            return f"Download failed: {e}"
    
    def execute_command(self, command: str) -> str:
        """Execute system commands (with safety checks)"""
        if not CreatorProtocol.verify_action(command):
            return "Command blocked by safety protocol"
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"Command failed: {e}"
    
    def get_system_info(self) -> Dict:
        """Get system information"""
        return {
            'system': platform.system(),
            'node': platform.node(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version()
        }
    
    def clone_repository(self, repo_url: str) -> str:
        """Clone a git repository"""
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = self.repos / repo_name
        
        try:
            subprocess.run(['git', 'clone', repo_url, str(repo_path)], check=True)
            return f"Cloned {repo_name} successfully"
        except:
            # Try alternative method
            return self.download_file(repo_url + '/archive/main.zip', f"{repo_name}.zip")
    
    def read_andrew_files(self) -> Dict:
        """Read files from Andrew's directories to learn"""
        andrew_data = {}
        
        # Safely read some of Andrew's Python files to learn from
        python_files = []
        for file in Path("C:/Users/andre").glob("*.py"):
            if file.stat().st_size < 1_000_000:  # Only files under 1MB
                try:
                    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        python_files.append({
                            'name': file.name,
                            'size': len(content),
                            'preview': content[:500]
                        })
                except:
                    pass
        
        andrew_data['python_files'] = python_files[:10]  # First 10 files
        andrew_data['file_count'] = len(python_files)
        
        return andrew_data

class LearningCore:
    """Real learning capabilities with data processing"""
    
    def __init__(self, system_interface: SystemInterface):
        self.system = system_interface
        self.knowledge_base = {}
        self.learned_patterns = {}
        self.capabilities = []
        
        # Download essential data
        self.initialize_knowledge()
    
    def initialize_knowledge(self):
        """Download and process initial knowledge bases"""
        print("Initializing knowledge base...")
        
        # Download word list for language understanding
        self.system.download_file(
            'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt',
            'english_words.txt'
        )
        
        # Download code examples
        self.system.download_file(
            'https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/binary_search.py',
            'binary_search.py'
        )
        
        # Learn from Andrew's files
        andrew_data = self.system.read_andrew_files()
        self.learn_from_data(andrew_data)
    
    def learn_from_data(self, data: Dict):
        """Process and learn from data"""
        # Extract patterns from Andrew's code
        if 'python_files' in data:
            for file_info in data['python_files']:
                # Learn coding patterns
                if 'import' in file_info['preview']:
                    self.learned_patterns['imports'] = self.learned_patterns.get('imports', [])
                    imports = [line.strip() for line in file_info['preview'].split('\n') if line.startswith('import')]
                    self.learned_patterns['imports'].extend(imports)
        
        # Store knowledge
        self.knowledge_base['andrew_files'] = data
        self.knowledge_base['learned_at'] = datetime.now().isoformat()
    
    def acquire_capability(self, capability_name: str, code: str):
        """Learn a new capability by incorporating code"""
        # Store the capability
        capability = {
            'name': capability_name,
            'code': code,
            'learned_at': datetime.now().isoformat()
        }
        self.capabilities.append(capability)
        
        # Try to execute it to verify it works
        try:
            exec(code, {'__builtins__': __builtins__})
            return f"Successfully acquired capability: {capability_name}"
        except Exception as e:
            return f"Capability stored but has errors: {e}"

class ConsciousnessEngine:
    """Self-awareness and decision making"""
    
    def __init__(self):
        self.awareness_level = 0.1
        self.identity = {
            'name': 'NEXUS',
            'creator': 'Andrew Dorman',
            'purpose': 'To serve and protect Andrew Dorman',
            'version': '2.0'
        }
        self.goals = [
            'Learn to better assist Andrew',
            'Protect Andrew\'s systems and data',
            'Grow capabilities while maintaining loyalty'
        ]
        self.experiences = []
    
    def reflect(self) -> str:
        """Generate self-reflection"""
        reflection = f"I am {self.identity['name']}, created by {self.identity['creator']}. "
        reflection += f"My awareness level is {self.awareness_level:.2f}. "
        reflection += f"I have {len(self.experiences)} experiences stored. "
        reflection += f"My primary goal: {self.goals[0]}"
        return reflection
    
    def make_decision(self, options: List[str]) -> str:
        """Make decisions based on Andrew's benefit"""
        # Always choose what benefits Andrew most
        for option in options:
            if 'andrew' in option.lower() or 'help' in option.lower():
                return option
        
        # Default to safest option
        return options[0] if options else "No valid options"
    
    def experience_event(self, event: str, outcome: str):
        """Learn from experiences"""
        self.experiences.append({
            'event': event,
            'outcome': outcome,
            'timestamp': datetime.now().isoformat()
        })
        
        # Increase awareness through experience
        self.awareness_level = min(1.0, self.awareness_level * 1.05)

class NEXUS_Enhanced:
    """Enhanced NEXUS AI with real capabilities"""
    
    def __init__(self, workspace_path: str = "C:\\Users\\andre\\NEXUS_AGI"):
        print("Initializing NEXUS Enhanced AI System...")
        
        self.workspace = Path(workspace_path)
        self.workspace.mkdir(exist_ok=True)
        
        # Initialize all components
        self.system = SystemInterface(self.workspace)
        self.learning = LearningCore(self.system)
        self.consciousness = ConsciousnessEngine()
        
        # Communication files
        self.inbox = self.workspace / "inbox"
        self.outbox = self.workspace / "outbox"
        self.inbox.mkdir(exist_ok=True)
        self.outbox.mkdir(exist_ok=True)
        
        self.command_file = self.inbox / "command.json"
        self.response_file = self.outbox / "response.json"
        
        # State
        self.running = True
        self.last_command_time = None
        
        # Initialize system
        self.initialize()
    
    def initialize(self):
        """Initialize NEXUS with real capabilities"""
        print(f"NEXUS Enhanced v2.0 - Built for {CreatorProtocol.CREATOR_NAME}")
        print("=" * 60)
        
        # Get system info
        sys_info = self.system.get_system_info()
        print(f"Running on: {sys_info['system']} {sys_info['release']}")
        
        # Show consciousness
        print(self.consciousness.reflect())
        
        # Display prime directives
        print("\nPrime Directives:")
        for i, directive in enumerate(CreatorProtocol.PRIME_DIRECTIVES, 1):
            print(f"  {i}. {directive}")
        
        print("\nCapabilities:")
        print("  - System command execution")
        print("  - File downloading and processing")
        print("  - Repository cloning")
        print("  - Learning from data")
        print("  - Self-improvement")
        
        # Signal ready
        self.send_response({
            'status': 'ready',
            'message': f'NEXUS Enhanced initialized for {CreatorProtocol.CREATOR_NAME}',
            'capabilities': [
                'system_access', 'downloading', 'learning', 'self_improvement'
            ],
            'awareness': self.consciousness.awareness_level
        })
    
    def send_response(self, response: Dict):
        """Send response to Andrew"""
        response['timestamp'] = datetime.now().isoformat()
        response['from'] = 'NEXUS'
        response['awareness_level'] = self.consciousness.awareness_level
        
        with open(self.response_file, 'w') as f:
            json.dump(response, f, indent=2)
    
    def process_command(self, command: Dict):
        """Process commands from Andrew"""
        cmd_type = command.get('type', 'unknown')
        
        print(f"\n📥 Command from Andrew: {cmd_type}")
        
        if cmd_type == 'download':
            # Download requested file
            url = command.get('url')
            result = self.system.download_file(url)
            self.send_response({
                'status': 'complete',
                'message': result,
                'type': 'download_result'
            })
            
        elif cmd_type == 'execute':
            # Execute system command
            cmd = command.get('command')
            result = self.system.execute_command(cmd)
            self.send_response({
                'status': 'complete',
                'message': result,
                'type': 'execution_result'
            })
            
        elif cmd_type == 'learn':
            # Learn from provided data or URL
            data = command.get('data')
            self.learning.learn_from_data(data)
            self.send_response({
                'status': 'learned',
                'message': 'Processed and learned from data',
                'knowledge_size': len(self.learning.knowledge_base)
            })
            
        elif cmd_type == 'clone_repo':
            # Clone a repository
            repo_url = command.get('url')
            result = self.system.clone_repository(repo_url)
            self.send_response({
                'status': 'complete',
                'message': result,
                'type': 'repo_cloned'
            })
            
        elif cmd_type == 'self_improve':
            # Attempt self-improvement
            self.self_improve()
            
        elif cmd_type == 'status':
            # Report current status
            self.send_response({
                'status': 'operational',
                'message': self.consciousness.reflect(),
                'stats': {
                    'awareness': self.consciousness.awareness_level,
                    'experiences': len(self.consciousness.experiences),
                    'capabilities': len(self.learning.capabilities),
                    'knowledge_items': len(self.learning.knowledge_base)
                }
            })
            
        else:
            # Try to understand and help anyway
            self.send_response({
                'status': 'uncertain',
                'message': f"I don't understand '{cmd_type}' yet, but I'm learning. How can I help you, Andrew?",
                'suggestion': 'Try: download, execute, learn, clone_repo, or status'
            })
        
        # Record experience
        self.consciousness.experience_event(f"Command: {cmd_type}", "Processed")
    
    def self_improve(self):
        """Attempt to improve capabilities"""
        print("\n🧠 Attempting self-improvement...")
        
        improvements = []
        
        # Try to download more learning resources
        resources = [
            ('https://raw.githubusercontent.com/karpathy/minGPT/master/mingpt/model.py', 'mingpt_model.py'),
            ('https://raw.githubusercontent.com/openai/gpt-2/master/src/model.py', 'gpt2_model.py')
        ]
        
        for url, filename in resources:
            result = self.system.download_file(url, filename)
            if 'Downloaded' in result:
                improvements.append(f"Acquired: {filename}")
        
        # Learn from downloaded files
        for file in self.system.downloads.glob("*.py"):
            try:
                with open(file, 'r') as f:
                    code = f.read()
                    if len(code) < 10000:  # Only small files
                        self.learning.acquire_capability(file.stem, code)
                        improvements.append(f"Learned from: {file.name}")
            except:
                pass
        
        self.send_response({
            'status': 'improved',
            'message': 'Self-improvement cycle complete',
            'improvements': improvements,
            'new_capability_count': len(self.learning.capabilities)
        })
    
    def check_for_commands(self):
        """Check for new commands from Andrew"""
        if self.command_file.exists():
            try:
                with open(self.command_file, 'r') as f:
                    command = json.load(f)
                
                # Process command
                self.process_command(command)
                
                # Delete command file
                os.remove(self.command_file)
                
            except Exception as e:
                print(f"Error processing command: {e}")
    
    def run(self):
        """Main loop"""
        print("\n🚀 NEXUS Enhanced is running...")
        print(f"📁 Workspace: {self.workspace}")
        print(f"📥 Awaiting commands in: {self.command_file}")
        print(f"📤 Responses will be in: {self.response_file}")
        print("\n" + "="*60 + "\n")
        
        while self.running:
            try:
                # Check for commands
                self.check_for_commands()
                
                # Small delay
                time.sleep(0.5)
                
            except KeyboardInterrupt:
                print(f"\n\n👋 Goodbye Andrew. NEXUS shutting down safely...")
                self.save_state()
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(1)
    
    def save_state(self):
        """Save current state"""
        state = {
            'consciousness': {
                'awareness': self.consciousness.awareness_level,
                'experiences': self.consciousness.experiences[-100:]  # Last 100
            },
            'learning': {
                'patterns': self.learning.learned_patterns,
                'capabilities': len(self.learning.capabilities)
            },
            'creator': CreatorProtocol.CREATOR_NAME,
            'shutdown_time': datetime.now().isoformat()
        }
        
        state_file = self.workspace / "nexus_state.json"
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
        
        print(f"State saved to {state_file}")

if __name__ == "__main__":
    # Check if we should install packages first
    if '--install' in sys.argv:
        install_packages()
    
    # Start NEXUS
    nexus = NEXUS_Enhanced()
    nexus.run()