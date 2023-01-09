import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexYearComponent } from './bissex-year.component';
import { HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import { By } from '@angular/platform-browser';

describe('BissexYearComponent', () => {
  let component: BissexYearComponent;
  let HttpMock: HttpTestingController;
  let fixture: ComponentFixture<BissexYearComponent>;
  let yeartbx: HTMLInputElement;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ BissexYearComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
    HttpMock = TestBed.get(HttpTestingController);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BissexYearComponent);
    component = fixture.componentInstance;

    const yeartbxDebugElement = fixture.debugElement.query(By.css('#yeartbx'));
    yeartbx = yeartbxDebugElement.nativeElement;
  });
  
  it('bissex_year: should show "..." in p on page launch', (() => {
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector("p").textContent).toContain("...");
  }));

  it('bissex_year: should make an HTTP GET request, and change DOM with bissextile year', (() => { 
    yeartbx.value = "2024"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_annee/?year=2024');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":true,"command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual("2024 est une année bissextile !");
  }));

  it('bissex_year: should make an HTTP GET request, and change DOM with non-bissextile year', (() => { 
    yeartbx.value = "2021"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_annee/?year=2021');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Year","command_entry":"2021","command_result":false,"command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual("2021 n'est pas une année bissextile.");
  }));

  it('bissex_year: should make an HTTP GET request, and change DOM with invalid entry', (() => { 
    yeartbx.value = "salut"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_annee/?year=salut');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":1,"command_type":"Bissex_Year","command_entry":"salut","command_result":null,"command_error":"Caractère(s) invalide(s)."});
    HttpMock.verify();
    expect(component.result).toEqual("Caractère(s) invalide(s).");
  }));
});

