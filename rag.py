import sys                      
import pathlib                  
import chromadb                 
from pypdf import PdfReader     
from anthropic import Anthropic 

# Datenbank im Ordner "db" anlegen bzw. öffnen. "docs" ist der Name der Sammlung darin.
client = chromadb.PersistentClient(path="db")
collection = client.get_or_create_collection("docs")


def chunk(text, size=800, overlap=100):
    """Zerlegt langen Text in Stücke von 800 Zeichen.
    Je 100 Zeichen überlappen, damit kein Satz an der Schnittkante verloren geht."""
    return [text[i:i + size] for i in range(0, len(text), size - overlap)]


def ingest():
    """Liest alle PDFs aus "docs", zerlegt sie und speichert die Stücke.
    Chroma berechnet dabei automatisch die Embeddings (Zahlenreihen, die die Bedeutung abbilden)."""
    for pdf in pathlib.Path("docs").glob("*.pdf"):
        text = "".join(page.extract_text() or "" for page in PdfReader(pdf).pages)
        chunks = chunk(text)
        collection.upsert(
            documents=chunks,                                       # die Textstücke
            ids=[f"{pdf.name}-{i}" for i in range(len(chunks))],    # eindeutiger Name pro Stück
            metadatas=[{"source": pdf.name}] * len(chunks),         # aus welcher Datei es stammt
        )
        print(f"{pdf.name}: {len(chunks)} Stücke gespeichert")


def ask(question):
    """Sucht die bis zu 6 Stücke, die der Frage am ähnlichsten sind (Retrieval),
    und lässt das Modell daraus eine Antwort formulieren (Generation)."""
    hits = collection.query(query_texts=[question], n_results=min(6, collection.count()))  # höchstens 6 Treffer
    context = "\n\n".join(
        f"[{meta['source']}] {doc}"
        for doc, meta in zip(hits["documents"][0], hits["metadatas"][0])
    )
    print("Quellen:", sorted({meta["source"] for meta in hits["metadatas"][0]}), "\n")
    answer = Anthropic().messages.create(
        model="claude-haiku-5-5",
        max_tokens=1500,
        messages=[{
            "role": "user",
            "content": "Beantworte die Frage nur anhand des Kontexts und nenne die Quelle. "
                       "Wenn die Antwort nicht im Kontext steht, sag das.\n\n"
                       f"Kontext:\n{context}\n\nFrage: {question}",
        }],
    )
    for block in answer.content:
        if block.type == "text":
            print(block.text)


# Startpunkt: entscheidet anhand deiner Eingabe, was passiert
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Nutzung: python rag.py ingest   oder   python rag.py "Deine Frage"')
    elif sys.argv[1] == "ingest":
        ingest()
    else:
        ask(" ".join(sys.argv[1:]))