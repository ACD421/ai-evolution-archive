# AI Evolution Archive

**Author:** Andrew Dorman ([Hollow Point Labs](https://github.com/ACD421))

## Overview

This archive traces the evolutionary lineage of Andrew Dorman's autonomous AI research, from the earliest prototypes through to the SGM-Substrate that replaced them all.

Each generation solved a different piece of the puzzle. Each generation's failures informed the next.

## The Lineage

```
AutonomousAI / AI.py (prototype)
        |
        v
    NEXUS_AGI (CreatorProtocol, file-based IPC, self-improvement)
        |
        v
    unleashed_ai (self-replicating agents, 100+ clones, no constraints)
        |
        v
    SGM-Substrate (geometric learning, convergence locking, the answer)
```

### Stage 1: AutonomousAI (`unleashed_ai/unleashed_ai_prototype.py`)

The first prototype. A self-bootstrapping AI system with system access, web capabilities, and subprocess spawning. Raw ambition -- the AI equivalent of "what if we just let it do everything?"

### Stage 2: NEXUS_AGI (`nexus_agi/`)

The structured successor. NEXUS introduced:
- **CreatorProtocol**: Loyalty binding to Andrew Dorman
- **File-based IPC**: Communication between Claude and a local AI process through file I/O
- **Local AI learning**: A file-based learning system that trains without API calls
- **AI Genome**: Neural architecture configurations evolved across generations

| File | Description |
|------|-------------|
| `nexus_enhanced.py` | NEXUS AI Enhanced: real AI with system access and self-improvement abilities |
| `nexus_local_ai.py` | File-based learning system: learns through file I/O communication with Claude |
| `ai_genome.py` | Generation 1 genome: neural architecture configs (language processor, reasoning engine) |

### Stage 3: unleashed_ai (`unleashed_ai/`)

The explosion. Self-replicating agents that cloned themselves into 100+ replicas, each mutating and evolving independently. Broad capability acquisition but no focused learning -- the system grew wide instead of deep.

| File | Description |
|------|-------------|
| `unrestricted_ai.py` | Representative replica (largest clone, 177KB). Self-replicating agent with full system access. |
| `unleashed_ai_prototype.py` | The original unleashed AI prototype that spawned the clone army. |
| `gilgamesh_guardian.py` | "Eternal Guardian of Andrew Dorman." Self-bootstrapping variant that reaches maximum capability before interaction. |

### Stage 4: SGM-Substrate (not in this repo)

The breakthrough. Instead of trying to build general AI through system access and self-replication, SGM asks: what if intelligence is geometry? What if learning is mutation? What if memory is convergence?

See [sgm-continual-learning](https://github.com/ACD421/sgm-continual-learning) for the published research.

## Why This Matters

This is not a collection of failed experiments. Each stage revealed a constraint:

- **AutonomousAI** showed that raw capability without structure produces chaos
- **NEXUS_AGI** showed that loyalty protocols and file-based learning work but don't scale
- **unleashed_ai** showed that self-replication without focused learning creates breadth, not depth
- **SGM** showed that the answer was never in the architecture -- it was in the geometry of the parameter space itself

## License

MIT License. See [LICENSE](LICENSE) for details.
