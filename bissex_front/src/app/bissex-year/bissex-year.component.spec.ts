import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexYearComponent } from './bissex-year.component';
import { By } from '@angular/platform-browser';

describe('BissexYearComponent', () => {
  let component: BissexYearComponent;
  let fixture: ComponentFixture<BissexYearComponent>;



  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexYearComponent ],
    })
    .compileComponents();

    fixture = TestBed.createComponent(BissexYearComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  it('should print the http response correctly', () => {
    const divresult = fixture.debugElement.query(By.css('.divresult'));
    expect(String(divresult)).toBe("salut")
  });
});

