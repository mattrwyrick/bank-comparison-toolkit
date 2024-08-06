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

        51: {
            "Name": "Financial Institution Name",
            "Street": "Financial Institution Address",
            "City": "Financial Institution City",
            "State": "Financial Institution State",
            "Zip": "Financial Institution Zip Code",
            "Report": "Financial Institution Filing Type"
        },
        41: {
            "Name": "Financial Institution Name",
            "Street": "Financial Institution Address",
            "City": "Financial Institution City",
            "State": "Financial Institution State",
            "Zip": "Financial Institution Zip Code",
            "Report": "Financial Institution Filing Type"
        },
        31: {
            "Name": "Financial Institution Name",
            "Street": "Financial Institution Address",
            "City": "Financial Institution City",
            "State": "Financial Institution State",
            "Zip": "Financial Institution Zip Code",
            "Report": "Financial Institution Filing Type"
        }
    }
}

RI_INFO = {
    NAME: "Interest Income",
    SCHED: "RI",
    MAPPING: {
        51: {
            "Total Loans": "RIAD4010",
            "Single Family Home Loans": "RIAD4435",
            "All Other Real Estate Loans": "RIAD4436",
            "C&I Loans": "RIAD4012"
        },
        41: {
            "Total Loans": "RIAD4010",
            "Single Family Home Loans": "RIAD4435",
            "All Other Real Estate Loans": "RIAD4436",
            "C&I Loans": "RIAD4012"
        },
        31: {
            "Total Loans": "RIAD4010",
            "Single Family Home Loans": "RIAD4435",
            "All Other Real Estate Loans": "RIAD4436",
            "C&I Loans": "RIAD4012"
        }
    }
}

RCK_INFO = {
    NAME: "Quarterly Loan Averages",
    SCHED: "RCK",
    MAPPING: {
        51: {
            "Total Loans": "RCON3360",
            "Single Family Home Loans": "RCON3465",
            "All Other Real Estate Loans": "RCON3466",
            "C&I Loans": "RCON3387"
        },
        41: {
            "Total Loans": "RCON3360",
            "Single Family Home Loans": "RCON3465",
            "All Other Real Estate Loans": "RCON3466",
            "C&I Loans": "RCON3387"
        },
        31: {  # RCFD
            "Total Loans": "RCON3360",
            "Single Family Home Loans": "RCON3465",
            "All Other Real Estate Loans": "RCON3466",
            "C&I Loans": "RCON3387"
        }
    }
}
