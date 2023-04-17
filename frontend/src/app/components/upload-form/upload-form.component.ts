import { Component, OnInit } from '@angular/core';
import { UploadService } from 'src/app/services/upload.service';

@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.css']
})
export class UploadFormComponent implements OnInit {

  selectedFiles: File[] = [];

  constructor(private uploadService: UploadService) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any) {
    this.selectedFiles = event.target.files;
  }

  onUpload() {
    const file = this.selectedFiles[0];
    this.uploadService.uploadFile(file).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
  }

}
