import { useNavigate } from "react-router";


function VoteEndPage(props:{text:string}) {
    const navigate = useNavigate();
    return (
        <div className="flex justify-center items-center flex-col bg-gray-50 dark:bg-gray-900 text-white">
            <div className="flex items-center justify-center flex-col h-screen">
                <h1 className="text-center text-2xl font-bold mb-4">{props.text} </h1>
                <button className="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Retour à la page d'accueil</button>
            </div>
        </div>
    )
}

export default VoteEndPage;