import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { take } from 'rxjs/operators';

@Component({
  selector: 'app-bissex-range',
  templateUrl: './bissex-range.component.html',
  styleUrls: ['./bissex-range.component.scss']
})
export class BissexRangeComponent {
  result! : string;
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.result = "..."
  }

  onSubmit() {
    const tbx1 = document.getElementById("year1tbx") as HTMLInputElement | null;
    const tbx2 = document.getElementById("year2tbx") as HTMLInputElement | null;
    this.http.get('http://0.0.0.0:8000/bissex_range/?year1=' + tbx1?.value + '&year2=' + tbx2?.value)
    .pipe(take(1))
    .subscribe(response => {
      const key = Object.keys(response) as Array<keyof typeof response>;
      if (String(response[key[3]]) == "")
      {
        this.result = String(response[key[4]]);
      }
      else if (String(response[key[3]]) == "[]")
      {
        this.result = "Aucune année n'est bissextile entre " + tbx1?.value + " et " + tbx2?.value + ".";
      }
      else
      {
        if(String(response[key[3]]).slice(1, -1).indexOf(",") > -1)
          this.result = String(response[key[3]]).slice(1, -1) + " sont des années bissextiles contenues dans l'intervale " + tbx1?.value + " - " + tbx2?.value + ".";
        else
          this.result = String(response[key[3]]).slice(1, -1) + " est une année bissextile contenue dans l'intervale " + tbx1?.value + " - " + tbx2?.value + ".";
      }
    });
  }
}