import { useEffect, useState } from "react"
import ApiService from "../service/ApiService";
import { useNavigate } from "react-router"; 

function CandidateChoice(){
    const [candidates, setCandidates] = useState<[string]>([""]);
    const [canVote, setCanVote] = useState<boolean>(true);
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchData(){
            setCandidates(await ApiService.getCandidatesForElection("4").then((response) => {
                if (response.data.length > 0 && response.data !== undefined) {
                    // case where there are actual candidates
                    return response.data[0]["list_of_candidates"];
                }
                setCanVote(false);
                return {};
            }));
        }
        fetchData();
        // console.log("À la fin du useEffect",candidates, canVote);
    }, [])
    
    const handleClick = () => {
        console.log("Je vais utiliser taquito pour envoyer ton vote sur la blockchain, tkt pas ça va bien se passer");

        // selon le status de taquito (si l'utilisateur a le droit de voter ou non)
        var res = true; 
        const link = res ? "done" : "error";
        navigate(link)
    }

    if (canVote){
        return (
            <div className="flex justify-center items-center flex-col bg-gray-50 dark:bg-gray-900 text-white" >
                <div className="flex items-center justify-center h-screen">
                    <div className="max-w-md">
                        <h1 className="text-center text-2xl font-bold mb-4">Votez parmi les propositions suivantes : </h1>
                            <div className="grid grid-cols-1 grid-flow-row  xl:grid-cols-2 mt-3">
                                {
                                    candidates.map((candidate, index) => (
                                        <div 
                                            key={index}
                                            className="hover:bg-primary-600 rounded-lg py-2 px-1 cursor-pointer text-lg text-center text-white" 
                                            onClick={handleClick}
                                        >
                                            {candidate}
                                        </div>
                                    ))
                                }
                            </div>
                    </div>
                </div>
            </div>
        )
    }
    else {
        return (
            <div>
                <h1>Page pour voter mec</h1>
                <div className="grid grid-cols-1 grid-flow-row  xl:grid-cols-2 mt-3">
                    <div>
                        On ne peut pas voter :'(.
                    </div>        
                </div>
            </div>
        )
    }
}

export default CandidateChoice;