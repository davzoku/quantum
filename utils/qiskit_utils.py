def get_status(provider):
    for backend in provider.backends():
        try:
            qubit_count = len(backend.properties().qubits)
        except:
            qubit_count = "simulated"
        print(f"{backend.name()} : {backend.status().pending_jobs} & {qubit_count} qubits")