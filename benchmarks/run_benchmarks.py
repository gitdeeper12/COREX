"""Run synthetic benchmark evaluation"""

import json
from generators.causal_chain import generate_causal_chain
from generators.spurious_confound import generate_spurious_confound
from generators.artifact_encoding import generate_artifact_encoding

def run_benchmarks(n_runs: int = 10):
    """Run all benchmarks"""
    results = {
        "causal": [],
        "spurious": [],
        "artifact": []
    }
    
    for run in range(n_runs):
        X, y = generate_causal_chain(seed=run)
        results["causal"].append({"run": run, "n_samples": len(X)})
        
        X, y = generate_spurious_confound(seed=run)
        results["spurious"].append({"run": run, "n_samples": len(X)})
        
        X, y = generate_artifact_encoding(seed=run)
        results["artifact"].append({"run": run, "n_samples": len(X)})
    
    with open("results/synthetic_1500.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Benchmarks complete: {len(results['causal'])} causal, "
          f"{len(results['spurious'])} spurious, {len(results['artifact'])} artifact")
    
    return results

if __name__ == "__main__":
    run_benchmarks()
