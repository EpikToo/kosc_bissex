import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexRangeComponent } from './bissex-range.component';
import { HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import { By } from '@angular/platform-browser';

describe('BissexRangeComponent', () => {
  let component: BissexRangeComponent;
  let HttpMock: HttpTestingController;
  let fixture: ComponentFixture<BissexRangeComponent>;
  let year1tbx: HTMLInputElement;
  let year2tbx: HTMLInputElement;


  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ BissexRangeComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
    HttpMock = TestBed.get(HttpTestingController);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BissexRangeComponent);
    component = fixture.componentInstance;

    const year1tbxDebugElement = fixture.debugElement.query(By.css('#year1tbx'));
    const year2tbxDebugElement = fixture.debugElement.query(By.css('#year2tbx'));

    year1tbx = year1tbxDebugElement.nativeElement;
    year2tbx = year2tbxDebugElement.nativeElement;

  });
  
  it('bissex_range: should show "..." in p on page launch', (() => {
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector("p").textContent).toContain("...");
  }));

  it('bissex_range: should make an HTTP GET request, and change DOM with multiple bissextile years', (() => { 
    year1tbx.value = "2020"
    year2tbx.value = "2025"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_range/?year1=2020&year2=2025');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Range","command_entry":"2020 - 2025","command_result":"[2020, 2024]","command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual("2020, 2024 sont des années bissextiles contenues dans l'intervale 2020 - 2025.");
  }));

  it('bissex_range: should make an HTTP GET request, and change DOM with a single bissextile year', (() => { 
    year1tbx.value = "2021"
    year2tbx.value = "2025"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_range/?year1=2021&year2=2025');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Range","command_entry":"2021 - 2025","command_result":"[2024]","command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual("2024 est une année bissextile contenue dans l'intervale 2021 - 2025.");
  }));

  it('bissex_range: should make an HTTP GET request, and change DOM with no bissextile year', (() => { 
    year1tbx.value = "2021"
    year2tbx.value = "2023"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_range/?year1=2021&year2=2023');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Range","command_entry":"2021 - 2023","command_result":"[]","command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual("Aucune année n'est bissextile entre 2021 et 2023.");
  }));

  it('bissex_range: should make an HTTP GET request, and change DOM with invalid entry', (() => { 
    year1tbx.value = "salut"
    year2tbx.value = "bonjour"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_range/?year1=salut&year2=bonjour');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":58,"command_type":"Bissex_Range","command_entry":"salut - bonjour","command_result":"","command_error":"Caractère(s) invalide(s)."});
    HttpMock.verify();
    expect(component.result).toEqual("Caractère(s) invalide(s).");
  }));
});

