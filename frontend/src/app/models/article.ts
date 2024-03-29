import { Genre } from "./genre"

export class Article{

    id:number = 0
    authors: string = ""
    year: number = 0
    title: string = ""
    journal: string = ""
    issue: number = 0
    place: string = ""
    doi: string = ""
    genreId: number = 0
    genre: Genre | undefined;
    pdf: string = ""
    pdfFile: any = ""

}