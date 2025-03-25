import pandas as pd
from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr
from datetime import datetime
if __name__ == "__main__": 
    build_experiment(
        experiment_name = "Leistungstest 1",
        date = datetime,
        supervisor = "Liliana Escobar",
        subject = "HR Test"
    )
    build_person(
        first_name = "Liliana",
        last_name = "Escobar",
        sex = "female",
        age = int(21)
    ) 
    estimate_max_hr(
        age_years = int(21),
        sex = "female"
    )
    def dic_komplett(patient, experiment):
        dic_komplett = {**patient, **experiment}
        return dic_komplett
    df = pd.DataFrame(dic_komplett)
    print(df)


$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
:
