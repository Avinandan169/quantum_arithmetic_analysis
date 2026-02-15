def circuit_metrics(qc):
    """
    Returns important circuit metrics for analysis.
    """

    ops = qc.count_ops()

    return {
        "depth": qc.depth(),
        "width": qc.width(),
        "cx_count": ops.get('cx', 0),
        "ccx_count": ops.get('ccx', 0),
        "total_gates": sum(ops.values())
    }