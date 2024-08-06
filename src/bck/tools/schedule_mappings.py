NAME = "Name"
SCHED = "Schedule"
MAPPING = "Mapping"

ID_1 = "IDRSSD"
ID_2 = "Bank ID"
ID_MAPPING = {ID_1: ID_2}

POR_INFO = {
    NAME: "Bank Info",
    SCHED: "POR",
    MAPPING: {
        "Name": "Financial Institution Name",
        "Street": "Financial Institution Address",
        "City": "Financial Institution City",
        "State": "Financial Institution State",
        "Zip": "Financial Institution Zip Code",
        "Report": "Financial Institution Filing Type"
    }
}

RI_INFO = {
    NAME: "Interest Income",
    SCHED: "RI",
    MAPPING: {
        "Total Loans": "RIAD4010",
        "Single Family Home Loans": "RIAD4435",
        "All Other Real Estate Loans": "RIAD4436",
        "C&I Loans": "RIAD4012"
    }
}

RCK_INFO = {
    NAME: "Quarterly Loan Averages",
    SCHED: "RCK",
    MAPPING: {
        "Total Loans": "RCON3360",
        "Single Family Home Loans": "RCON3465",
        "All Other Real Estate Loans": "RCON3466",
        "C&I Loans": "RCON3387"
    }
}
